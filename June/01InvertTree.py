class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return


s = Solution();
t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(7)
t4 = TreeNode(1)
t5 = TreeNode(3)
t6 = TreeNode(6)
t7 = TreeNode(9)

t2.left = t4
t2.right = t5
t1.left = t2
t1.right = t3
print(s.invertTree([4, 1, 2, 1, 2]))
