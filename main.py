from PyQt6.QtWidgets import QApplication
from gui import GameWindow
import sys

def main():
    app = QApplication([])
    gameWindow = GameWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()