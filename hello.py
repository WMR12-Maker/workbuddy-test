#!/usr/bin/env python3
"""GitHub 连接冒烟测试脚本。"""

import platform
import sys
from datetime import datetime


def main() -> None:
    print("=" * 40)
    print("  Hello from workbuddy-test!")
    print("=" * 40)
    print(f"时间     : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Python   : {sys.version.split()[0]}")
    print(f"操作系统 : {platform.system()} {platform.release()}")
    print(f"机器架构 : {platform.machine()}")
    print("=" * 40)


if __name__ == "__main__":
    main()
