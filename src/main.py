import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSharedMemory

from model.blivedmmodel import BLiveModel

from modelview.blive import Blive

from ui.MainWindow import MainWindow as MainWindow

def main():
    # 确保程序启动唯一
    shared_memory = QSharedMemory("M7GA")
    if not shared_memory.create(1):
        print("已经有其他实例在运行.")
        sys.exit(0)

    # 启动应用程序
    app = QApplication(sys.argv)

    # model = BLiveModel()
    blive = Blive(BLiveModel())
    mainWindow = MainWindow(blive)
    mainWindow.show()
    blive.start_blive()
    # mainWindow.start_blive()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
