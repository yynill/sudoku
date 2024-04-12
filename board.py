class Board:
    def __init__(self):
        self.grid = [[0]*9 for _ in range(9)]

    def print_board(self):
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(val)
                else:
                    print(val, end=" ")
