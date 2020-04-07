from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices) ):
            # print (i)
            # print(prices[i],prices[i - 1],sep=",")
            if (prices[i] - prices[i - 1]) >  0:
                profit += prices[i] - prices[i - 1]

        print (profit)
        return profit

s1 = Solution();
s1.maxProfit([7,1,5,3,6,4])
