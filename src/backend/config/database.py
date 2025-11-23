"""
数据库配置（Tortoise-ORM）
"""

import sys
from pathlib import Path

from aerich import Command
from loguru import logger
from tortoise import Tortoise

from .settings import settings

# Tortoise-ORM配置
TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "src.features.user.backend.models",
                # 在此添加其他功能模块的models
                "aerich.models",  # Aerich迁移管理
            ],
            "default_connection": "default",
        },
    },
}


async def run_migrations():
    """
    运行 Aerich 数据库迁移
    仅在 Windows 桌面应用环境 (frozen) 且使用 SQLite 时调用
    """
    try:
        # 1. 确定 migrations 目录位置
        if getattr(sys, "frozen", False):
            # 打包环境: _internal/migrations
            base_dir = Path(sys.executable).parent
            migrations_dir = base_dir / "migrations"
        else:
            # 开发环境: 项目根目录/migrations
            migrations_dir = Path("migrations")

        if not migrations_dir.exists():
            logger.warning(
                f"⚠️ Migrations directory not found at {migrations_dir}, skipping migrations.",
            )
            return

        logger.info(f"🔄 Running migrations from {migrations_dir}...")

        # 2. 初始化 Aerich Command
        command = Command(tortoise_config=TORTOISE_ORM, location=str(migrations_dir))

        # 3. 初始化数据库连接 (Aerich 需要)
        await command.init()

        # 4. 尝试初始化 aerich 表 (如果不存在)
        # safe=True 保证如果表已存在不报错
        # 这通常用于首次安装
        await command.init_db(safe=True)

        # 5. 执行升级
        # run_in_transaction=True 保证原子性
        await command.upgrade(run_in_transaction=True)

        logger.success("✅ Database migrations applied successfully.")

    except Exception as e:
        logger.exception(f"❌ Failed to run migrations: {e}")
        # 在桌面应用中，迁移失败可能意味着数据损坏或版本不兼容
        # 但我们尽量不让应用崩溃，而是记录错误


async def init_db():
    """
    初始化数据库连接
    在应用启动时调用
    """
    await Tortoise.init(config=TORTOISE_ORM)

    # 策略：
    # 1. 开发环境：总是尝试生成表结构 (快速开发)
    # 2. 生产环境且使用 SQLite（桌面版场景）：使用 Aerich 迁移系统
    # 3. 生产环境且使用服务器数据库：应手动使用 Aerich 迁移工具

    is_sqlite = settings.DATABASE_URL.startswith("sqlite://")
    is_frozen = getattr(sys, "frozen", False)

    if settings.ENVIRONMENT == "development" and not is_frozen:
        # 开发环境：自动建表 (如果不使用 aerich)
        # safe=True: 如果表已存在则忽略
        logger.info("🔧 Development mode: Generating schemas...")
        await Tortoise.generate_schemas(safe=True)

    elif is_sqlite and is_frozen:
        # 桌面版生产环境：自动迁移
        await run_migrations()
