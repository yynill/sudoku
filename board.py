import random


class Board:
    def __init__(self):
        self.grid = [["."]*9 for _ in range(9)]

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

    def generateRandomStart(self):
        filled_cells = 0
        while filled_cells < 17:
            randNumber = random.randint(1, 9)
            randRow = random.randint(0, 8)
            randCol = random.randint(0, 8)

            if self.grid[randRow][randCol] == "." and self.validateCell(randNumber, randRow, randCol):
                self.grid[randRow][randCol] = randNumber
                filled_cells += 1

    def validateCell(self, randNumber, randRow, randCol):
        # Check horizontally
        for i in range(9):
            if self.grid[randRow][i] == randNumber:
                return False

        # Check vertically
        for i in range(9):
            if self.grid[i][randCol] == randNumber:
                return False

        # Check 3x3 box
        # top left cell in the 3x3 box
        startRow = randRow // 3 * 3
        startCol = randCol // 3 * 3

        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if self.grid[i][j] == randNumber:
                    return False

        return True

    def solve(self):  # back tracking algorithm
        # find all free cells
        freeCells = []
        for i in range(0, 81):
            row = i//9
            col = i % 9
            if self.grid[row][col] == ".":
                freeCells.append((row, col))
        print(freeCells)

        index = 0
        found = False
        while index < len(freeCells):
            row, col = freeCells[index]
            num = self.grid[row][col]

            if num == ".":
                num = 0  # empty, start trying from 1
            found = False

            for n in range(num+1, 10):
                if self.validateCell(n, row, col):
                    self.grid[row][col] = n
                    index += 1  # Move to the next cell
                    found = True
                    break

            if not found:  # If no valid number was found, backtrack
                if index == 0:
                    return False  # Unsolvable
                self.grid[row][col] = "."
                index -= 1
        return True
