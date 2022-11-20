from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QGridLayout, QFrame
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QLine
from TicFrame import TicFrame
from TicLogic import Controller
MIN_W = 256
MIN_H = 256
WINDOW_TITLE = "Tic-Tac-Toe"
RGB_BLACK = "#000000"

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(MIN_W, MIN_H)
        self.setWindowTitle(WINDOW_TITLE)
        self.controller = Controller()
        self.frameList = []
        self.setGridLayout()
        self.setLayout(self.horizontalGroupBox)
        
        self.show()
        
    def setGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setContentsMargins(0,0,0,0)
        
        layout.setSpacing(0)

        positions = [(x,y) for x in range(3) for y in range(3)]
        
        for index, position in enumerate(positions):
            self.frameList.append(TicFrame(self.controller, *position))
            layout.addWidget(self.frameList[index], *position)
        print([(f.x, f.y) for f in self.frameList])
        self.horizontalGroupBox = layout
        
    @property 
    def height(self) -> int:
        return self.size().height()
        
    @property
    def width(self) -> int:
        return self.size().width()
    
    def mouseReleaseEvent(self, event, x, y):
        print('pressed')
        won = self.controller.check_win(x, y, self.frameList)
        if won:
            print("YOU WON")

    