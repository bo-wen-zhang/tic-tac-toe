from enum import Enum

#game has to be over when 9 moves has been played, check 

class State(Enum):
    BLANK = 'white'
    X = 'red'
    O = 'blue'


class Controller():
    def __init__(self) -> None:
        self.current_player = State.X
        
    def next_turn(self) -> None:
        if self.current_player == State.X:
            self.current_player = State.O
        else:
            self.current_player = State.X
        
    def check_win(self, x, y, frameList):
        #any tile would need to check if the horizontal line is the same
        vert_complete = self.check_vert(y, frameList)
        hori_complete = self.check_hori(x, frameList)
        diag_complete = self.check_diag(x, y, frameList)
        #if it is a center tile it will also need to check the diagonals
        if any([vert_complete, hori_complete, diag_complete]):
            #finish game
            print("won")
            return True
        else:
            self.next_turn()
            return False

        
    
    def check_vert(self, y, frameList):
        column_states = [frameList[index].state for index in range(len(frameList)) if index % 3 == y]
        complete = len(set(column_states)) == 1
        print(complete)
        return complete

    def check_hori(self, x, frameList):
        row_states = [frameList[index].state for index in range(len(frameList)) if x*3 <= index and index < (x+1)*3]
        complete = len(set(row_states)) == 1
        return complete
    
    def check_diag(self, x, y, frameList):
        fwd_complete, bwd_complete = False, False
        if x == y:
            diag_states = [frameList[index].state for index in range(len(frameList)) if index % 4 == 0]
            fwd_complete = len(set(diag_states)) == 1
        if x + y == 2:
            diag_states = [frameList[index].state for index in range(len(frameList)-1) if index % 2 == 0]
            bwd_complete = len(set(diag_states)) == 1
        return fwd_complete or bwd_complete
        
class Board():
    def __init__(self):
        return
        


    
    
    
        