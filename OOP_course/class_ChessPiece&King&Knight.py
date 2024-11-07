from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self):
        pass


class Knight(ChessPiece):

    def can_move(self, horizontal, vertical):
        if abs((ord(horizontal) - 97) - (ord(self.horizontal) - 97)) * abs(vertical - self.vertical) == 2:
            return True
        else:
            return False

class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        if self.horizontal == horizontal and self.vertical == vertical:
            return False
        else:
            temp_hor = abs((ord(horizontal) - 96) - (ord(self.horizontal) - 96))
            temp_ver = abs(self.vertical - vertical)
            return temp_hor <= 1 and temp_ver <= 1