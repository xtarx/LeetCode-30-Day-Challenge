from typing import List


class BinaryMatrix(object):
    m = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 1]]
    acc = 0

    def get(self, x: int, y: int) -> int:
        self.acc += 1
        return self.m[x][y]

    def dimensions(self) -> List:
        return [len(self.m), len(self.m[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        currentRow = 0
        currentColumn = cols - 1

        # if 1 move left,otherwise move down
        while currentRow < rows and currentColumn > -1:
            if binaryMatrix.get(currentRow, currentColumn) == 1:
                currentColumn -= 1
            else:
                currentRow += 1

        print("called", binaryMatrix.acc)
        if currentColumn != cols - 1:
            return currentColumn + 1

        return -1


s = Solution();
m = BinaryMatrix()
print(s.leftMostColumnWithOne(m))
