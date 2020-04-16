from typing import List
from functools import reduce
class Solution:

    def checkValidString2(self, s: str) -> bool:
        p1=0
        p2=len(s)-1

        # while p1 != p2:
        while p1 < p2:
            print("while",p1,p2)
            if not self.matchingPair(s[p1],s[p2]):
                return False

            p1+=1
            p2-=1
        return True


    def replaceWild(self,s:str):
        leftParent=s.count("(")
        rightParent=s.count(")")
        starParent=s.count("*")
        print(leftParent,rightParent,starParent)

    def checkValidString(self, s: str) -> bool:


        leftParent = s.count("(")
        rightParent = s.count(")")
        starParent = s.count("*")

        if not starParent and leftParent!=rightParent:
            return False;

    

        mystack=[]
        mystack.append(s[0])
        for c in s[1:]:
            if  len(mystack)==0:
                mystack.append(c)
            else:
                top=mystack[-1]
                if top =="(":
                    mystack.pop()
                else:
                    mystack.append(c)

        return len(mystack)==0

    def matchingPair(self,c1,c2) -> bool:
        print("matchingPair", c1 , c2)
        if c1 == "(":
            return  c2 == ")" or c2 == "*"
        # if c1 == ")":
        #     return  c2 == "(" or c2 == "*"
        if c1 == "*":
            return  c2 == "(" or c2 == ")"

s = Solution();
print(s.checkValidString("(()"))
# print(s.checkValidString("(*))"))
# print(s.checkValidString("()"))
# print(s.checkValidString("()()"))
