from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZeroInd=[]
        for index, value in enumerate(nums):
                if value != 0:
                    nonZeroInd.append(index)
        j=len(nums)-1
        for i in range(len(nonZeroInd)):
            nums[i] = nums[nonZeroInd[i]]

        for i in range(len(nums)-len(nonZeroInd)):
            nums[j] = 0
            j=j-1



        # print(nonZeroInd)
        # print(nums)


s1 = Solution();
s1.moveZeroes([0, 1, 0, 3, 12])
