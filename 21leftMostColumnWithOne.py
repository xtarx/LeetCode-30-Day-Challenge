from typing import List


class BinaryMatrix(object):
    # m = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
    # m=
    acc = 0

    def get(self, x: int, y: int) -> int:
        self.acc += 1
        return self.m[x][y]

    def dimensions(self) -> List:
        return [len(self.m), len(self.m[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        m, n = binaryMatrix.dimensions()
        print(m, n)
        rowsSums = dict()
        lastColZerosCount = 0
        # check if the last column has any 1s, if not then return -1
        for x in range(0, m):
            if binaryMatrix.get(x, n - 1) > 0:
                rowsSums[x] = rowsSums.get(x, 0) + 1
                # break
            else:
                lastColZerosCount += 1

        if lastColZerosCount == m:
            return -1
        # print(rowsSums)
        for x in range(0, m):
            for y in range(n - 2, -1, -1):
                if binaryMatrix.get(x, y) > 0:
                    rowsSums[x] = rowsSums.get(x, 0) + 1
                else:
                    break

        # print(rowsSums)
        print("BinaryMatrix.get() called:", binaryMatrix.acc)

        return n - max(rowsSums.values())


s = Solution();
m = BinaryMatrix()
print(s.leftMostColumnWithOne(m))
