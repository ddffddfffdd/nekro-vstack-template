import os
import sys
import webbrowser
from pathlib import Path

import uvicorn

from src.backend.config.settings import settings
from src.backend.main import app


def resolve_static_path():
    """解析静态文件路径（兼容开发环境和打包环境）"""
    if getattr(sys, "frozen", False):
        # 打包环境: _internal/static
        # PyInstaller 在单目录模式下，数据在 _internal 下（如果打包成单文件则在临时目录）
        return Path(sys.executable).parent / "static"
    # 开发环境
    return Path(__file__).resolve().parents[2] / "dist"


def main():
    """桌面端启动入口"""
    # 覆盖静态文件路径检测逻辑 (在 main.py 中已经有处理，这里主要是确保环境变了设置正确)
    # 实际上 main.py 里的 static_dir = Path("/app/static") 是针对 Docker 的
    # 我们需要在启动时动态修改这个路径，或者让 main.py 更智能

    # 更好的方式是设置环境变量，让 settings 或 main 读取
    # 但 main.py 里的 Path("/app/static") 是硬编码的。
    # 让我们修改 main.py 来支持动态配置静态目录

    # 启动浏览器
    host = settings.HOST
    port = settings.PORT
    url = f"http://{host}:{port}"

    print(f"🚀 Starting Desktop App at {url}")

    # 延迟打开浏览器，确保服务已启动
    # 注意：uvicorn.run 是阻塞的，所以不能在之后运行
    # 我们可以用 Timer 或者 startup event，或者简单的在 run 之前打开（浏览器会重试或等待）
    import threading
    import time

    def open_browser():
        time.sleep(2)  # 等待 2 秒
        webbrowser.open(url)

    threading.Thread(target=open_browser, daemon=True).start()

    # 启动服务
    # 注意：在 PyInstaller 打包应用中，reload 必须为 False
    uvicorn.run(app, host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
