import widget

class Checker(object):
    __board = widget.Board()
    __translate = False

    def check_move(self, old , new = None):
        "Checks whether a given move is legal"
        if new == None:
            old, new = old

        return self.__board.check_move(old, new)

    def make_move(self, old, new = None):
        '''Updates the board state, without checking the move's legality'''
        if new == None:
            old, new = old

        self.__board.move_piece(old, new)
