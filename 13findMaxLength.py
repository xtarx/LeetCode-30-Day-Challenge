from typing import List


class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        stack = []
        count = 0
        maxContiguous = 0
        stack.append(nums[0])

        for i in range(1, len(nums)):
            print('index:', i)
            if len(stack) < 1 or nums[i] == stack[-1]:
                stack.append(nums[i])

            else:
                stack.pop()

            if len(stack) == 0:
                numOnes = self.countOnes(nums[0:i + 1])
                if numOnes > maxContiguous:
                    maxContiguous = numOnes
                count += 1

        # return count * 2
        return maxContiguous * 2

    def countOnes(self, nums: List[int]) -> int:
        print("Count ones received: ", nums)
        numOnes = 0
        for i in nums:
            if i == 1:
                numOnes += 1
        return numOnes


s = Solution();
# print(s.findMaxLength([0, 0, 0, 1, 1, 1, 0]))
# print(s.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))
print(s.findMaxLength([0, 1, 0]))
