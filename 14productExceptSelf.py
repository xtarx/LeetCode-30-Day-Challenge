from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]

        # first item
        output.append(self.multiplyList(nums[1:]))

        for i in range(1,len(nums)-1):
            # swap current index with index[0]
            # nums[i], nums[0] = nums[0], nums[i]
            # all what before me * all what after me
            before=nums[:i]
            after=nums[i+1:]
            # print("before",before)
            # print("after",after)
            prod=self.multiplyList(before) *self.multiplyList(after)
            # print(prod)
            output.append(prod)
        # last item
        output.append(self.multiplyList(nums[:-1]))
        return output

    def russian_peasant(self,x, y):
        z = 0
        while y > 0:
            if y % 2 == 1: z = z + x
            x = x << 1
            y = y >> 1
        return z

    def multiplyList(self,myList):
        result = 1
        for x in myList:
            result = self.russian_peasant(result,x)
        return result


s = Solution();
print(s.productExceptSelf([1,2,3,4]))
