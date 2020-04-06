from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numCount=dict()
        for n in nums:
            if n in numCount and numCount[n] > 0:
                numCount.pop(n)
            else:
                numCount[n]=1
        return next(iter(numCount));



s1=Solution()
print(s1.singleNumber([4,1,2,1,2]))

