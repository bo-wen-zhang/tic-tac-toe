from PyQt6.QtWidgets import QFrame
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QSizePolicy
from TicLogic import Controller, State

class TicFrame(QFrame):
    def __init__(self, controller : Controller , x , y): 
        super().__init__()
        self.controller = controller
        self.x = x
        self.y = y
        self.state = State.BLANK
        #self.palette = palette()
        self.palette = self.palette()
        self.palette.setColor(self.backgroundRole(), QColor(self.state.value))
        self.setPalette(self.palette)
        self.setAutoFillBackground(True)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.setFrameStyle(QFrame.Shape.Panel)
        self.setLineWidth(3)
        
    def mouseReleaseEvent(self, event):
        print(self)
        if self.state != State.BLANK:
            print('not blank')
            return
        current_player = self.controller.current_player
        #try find a more efficient way of changing the colour
        self.palette.setColor(self.backgroundRole(), QColor(current_player.value))
        self.setPalette(self.palette)
        
        self.state = current_player
        
        #pyqt child consumes the event, so we need to pass the event along to parent
        self.parent().mouseReleaseEvent(event, self.x, self.y)
        
    def __str__(self):
        return f'position x: {self.x} position y: {self.y} state: {self.state.value}'