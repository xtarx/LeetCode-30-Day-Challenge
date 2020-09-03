from typing import List
import sys
iMaxStackSize = 5000
sys.setrecursionlimit(iMaxStackSize)

class Solution:
    def isHappy(self, n: int) -> bool:
        # print (int(str(n)[0]))
        sum = self.sum_digits_squared(n)
        if sum == 1:
            return True
        try:
            return self.isHappy(sum);
        except:
            return False

    @staticmethod
    def sum_digits_squared(n):
        s = 0
        while n:
            s += pow(n % 10,2)
            n //= 10
        return s
s1=Solution()
print(s1.isHappy(129))

