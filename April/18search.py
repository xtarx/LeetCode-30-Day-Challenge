from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] <= nums[right]:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

    def searchRecursive(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.searchHelper(nums, target, left, right)

    def searchHelper(self, nums: List[int], target: int, left: int, right: int) -> int:
        middle = (left + right) // 2
        if left > right:
            return -1
        if target == nums[middle]:
            return middle
        # check left half if sorted it has the key
        elif nums[left] <= nums[middle]:
            # left half is sorted then check if target is in that range, else go to the right half
            if nums[left] <= target <= nums[middle]:
                return self.searchHelper(nums, target, left, middle - 1)
            else:
                #  else go to the right half
                return self.searchHelper(nums, target, middle + 1, right)
            # right = middle - 1
        # right half is sorted then check if target is in that range, else go to the left half
        else:
            if nums[middle] <= target <= nums[right]:
                return self.searchHelper(nums, target, middle + 1, right)
            else:
                #  else go to the left half
                return self.searchHelper(nums, target, left, middle - 1)
        return -1


s = Solution();
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([3, 1], 1))
