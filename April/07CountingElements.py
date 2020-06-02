import collections
from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash=dict()
        count=0
        for i in arr:
            hash[i]=1

        for i in arr:
            if (i+1) in hash:
                count+=1
        return count


    # def countElements(self, arr: List[int]) -> int:
    # # collections.defaultdict()
    # doubleArr = []
    # for i in arr:
    #     doubleArr.append(i+1)
    # count=0
    # for  i in doubleArr:
    #     if arr.count(i)>0:
    #         count+=1
    # # print(doubleArr)
    # return count


s1 = Solution();
print(s1.countElements([1,1,2,2]))
# print(s1.countElements([1,1,2,2]))
