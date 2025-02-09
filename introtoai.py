class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.box_size = 3

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid_move(self, row, col, num):
        # Check row
        for x in range(self.size):
            if self.board[row][x] == num and col != x:
                return False

        # Check column
        for x in range(self.size):
            if self.board[x][col] == num and row != x:
                return False

        # Check 3x3 box
        box_row = row - row % self.box_size
        box_col = col - col % self.box_size

        for i in range(box_row, box_row + self.box_size):
            for j in range(box_col, box_col + self.box_size):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False

        return True

    def print_board(self):
        for i in range(self.size):
            if i % self.box_size == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(self.size):
                if j % self.box_size == 0 and j != 0:
                    print("|", end=" ")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

# Create and solve a Sudoku puzzle
if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    print("Original Puzzle:")
    solver = SudokuSolver(puzzle)
    solver.print_board()

    print("\nSolving...\n")

    if solver.solve():
        print("Solved Puzzle:")
        solver.print_board()
    else:
        print("No solution exists")