# pyinstaller_hooks/hook-pyside6.py
import os
import PySide6

# 告诉 PyInstaller PySide6 的安装位置
pyside6_dir = os.path.dirname(PySide6.__file__)

# 收集 PySide6 的所有二进制文件（DLLs）和插件
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_submodules, collect_data_files

# 收集动态链接库 (.dll, .so, .dylib)
binaries = collect_dynamic_libs("PySide6")

# 收集所有子模块（防止 ImportError）
hiddenimports = collect_submodules("PySide6")

# 收集 Qt 的插件（如 platforms/qwindows.dll，这是必须有的，否则黑屏）
datas = collect_data_files("PySide6", include_py_files=False)