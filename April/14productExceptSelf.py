from typing import List
from functools import reduce
class Solution:


    def productExceptSelf3(self, nums):
        size = len(nums)
        ary_left = [1] * size
        ary_right = [1] * size
        ary_res = []
        for i in range(size - 1):
            ary_left[i + 1] *= ary_left[i] * nums[i]

        for i in range(size - 1, 0, -1):
            ary_right[i - 1] *= ary_right[i] * nums[i]

        for i in range(size):
            ary_res.append(ary_left[i] * ary_right[i])
        return ary_res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]

        # first item
        output.append(reduce(lambda x, y: x*y,(nums[1:])))

        for i in range(1,len(nums)-1):
            # swap current index with index[0]
            # nums[i], nums[0] = nums[0], nums[i]
            # all what before me * all what after me
            before=nums[:i]
            after=nums[i+1:]
            # print("before",before)
            # print("after",after)
            # prod=self.multiplyList(before) *self.multiplyList(after)
            prod=reduce(lambda x, y: x*y,before)*reduce(lambda x, y: x*y,after)
            # print(prod)
            output.append(prod)
        # last item
        output.append(reduce(lambda x, y: x*y,(nums[:-1])))

        return output



s = Solution();
print(s.productExceptSelf3([1,2,3,4]))
