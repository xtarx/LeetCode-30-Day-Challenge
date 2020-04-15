from typing import List
import math

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        stringAsList=[]
        for c in s:
            stringAsList.append(c)
        for move in shift:
            if move[0] > 0:
                stringAsList=self.shiftRight(stringAsList,move[1])
            else:
                stringAsList=self.shiftLeft(stringAsList, move[1])

        return ''.join(stringAsList)

    def shiftLeft(self,s:List[str],amount) -> List[str]:
        for i in range(amount):
            first=s.pop(0)
            s.append(first)
        return s

    def shiftRight(self,s:List[str],amount) -> List[str]:
        for i in range(amount):
            last=s.pop()
            s.insert(0,last)
        return s

s = Solution();
# print(s.shiftRight(["a","b","c"],2))
print(s.stringShift("abc",[[0,1],[1,2]]))
print(s.stringShift("abcdefg",[[1,1],[1,1],[0,2],[1,3]]))
