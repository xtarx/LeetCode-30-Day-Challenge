from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort(reverse=True)

        while True:
            if len(stones) == 1:
                break
            n1 = stones.pop(0)
            n2 = stones.pop(0)
            stones.append(n1 - n2)
            stones.sort(reverse=True)

        return stones[0]


s = Solution();
print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
