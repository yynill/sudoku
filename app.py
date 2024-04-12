from board import Board

if __name__ == '__main__':
    sudoku_board = Board()
    sudoku_board.generateRandomStart()
    sudoku_board.print_board()
