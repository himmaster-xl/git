"""
Git 操作练习脚本
一个简单的文件管理器，演示 Git 版本控制的基本概念
"""

import os
import sys
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('file_manager.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


def show_info():
    """显示当前工作目录信息"""
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print(f"📍 当前目录: {cwd}")
    print(f"📁 文件数量: {len(files)}")
    print(f"🕐 当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return files


def list_files(path="."):
    """列出目录下所有文件"""
    items = os.listdir(path)
    print(f"\n📂 {os.path.abspath(path)} 下的内容:")
    print("-" * 40)
    for item in sorted(items):
        full_path = os.path.join(path, item)
        item_type = "📁" if os.path.isdir(full_path) else "📄"
        size = os.path.getsize(full_path) if os.path.isfile(full_path) else 0
        print(f"  {item_type} {item:<25s} {size:>6d} bytes")
    print("-" * 40)


def main():
    logging.info("脚本启动")
    print("=" * 40)
    print("🐍 Git 练习脚本 v1.0")
    print("=" * 40)

    files = show_info()
    list_files()
    logging.info(f"共列出 {len(files)} 个文件")

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            list_files(path)
        else:
            print(f"❌ 路径不存在: {path}")
    else:
        print("\n💡 提示: 可以传入路径参数来查看指定目录")
        print("   用法: python git.py <目录路径>")


if __name__ == "__main__":
    main()
