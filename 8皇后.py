class solution(object):
    def queens_sum(self, n):
        self.position([-1] * n, 0, n)

    def position(self, col, row, n):
        if row == n:
            self.printSolution(col, n)
            return

        for row_position in range(n):
            col[row] = row_position
            if self.isValid(col, row):
                self.position(col, row + 1, n)

    def isValid(self, col, row):
        if len(set(col[:row + 1])) != len(col[:row + 1]):
            return False

        for i in range(row):
            if abs(col[i] - vol[row]) == int(row - 1):
                return False
            return True

    def printSolution(self, col, n):
        print(col, '\n')
        for row in range(n):
            line = ""
            for column in range(n):
                if col[row] == column:
                    line += " Q "
                else:
                    line += " * "
            print(line)
        print('\n')
def main():
    q = solution()
    q.queens_sum(8)

if __name__ == '__mian__':
    main()