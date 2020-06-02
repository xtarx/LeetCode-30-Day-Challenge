import collections
from typing import List


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        s=""
        t=""
        for c in S:
            if c=="#":
                s=s[:-1]
            else:
                s=s+c
        for c in T:
            if c=="#":
                t=t[:-1]
            else:
                t=t+c
        return s==t
s1 = Solution();
print(s1.backspaceCompare("ab#c","ad#c"))
