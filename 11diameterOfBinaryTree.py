# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.arr = []

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return max(self.findDepth(root.left,1),self.findDepth(root.right,1))
        elif root.left is None:
            return self.findDepth(root.right, 1)
        else:
            return self.findDepth(root.left, 1)

    def findDepth(self, root: TreeNode, count) -> int:
        count = count + 1
        # print(count)
        if root is None:
            return count

        if root.left:
            return  self.findDepth(root.left, count)
        if root.right:
            return  self.findDepth(root.right, count)


s = Solution();
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t2.left = t4
t2.right = t5
t1.left = t2
t1.right = t3

print(s.diameterOfBinaryTree(t1))

# print(s1.diameterOfBinaryTree("ab#c","ad#c"))
