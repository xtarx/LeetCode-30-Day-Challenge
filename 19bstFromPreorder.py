from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    preIndex = 0

    def __init__(self):
        preIndex = 0

    def bstHelper(self, pre, low, high, size) -> TreeNode:
        if low > high or self.preIndex >= size:
            return None

        # root is always the first item in the list

        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        # if list has only 1 item then return
        if low == high:
            return root;

        # find the first value which is bigger than the root, the  use it as a pivot
        for i in range(low, high + 1):
            if pre[i] > root.val:
                break

        # do the pivot

        root.left = self.bstHelper(pre, self.preIndex, i - 1, size)
        root.right = self.bstHelper(pre, i, high, size)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        r = self.bstHelper(preorder, 0, len(preorder) - 1, len(preorder))
        # self.printPostorder(r)
        # print(self.printLevelOrder(r))
        # self.printPreorder(r)
        return r
        # return 1

    def printLevelOrder(self, root):
        # Base Case 
        if root is None:
            return

        # Create an empty queue for level order traversal 
        queue = [root]

        # Enqueue Root and initialize height

        while len(queue) > 0:
            # Print front of queue and remove it from queue 
            print(queue[0].val)
            node = queue.pop(0)

            # the null case
            # parent has one left and no right
            # or parent has one right and no left

            # Enqueue left child 
            if node.left is not None:
                queue.append(node.left)
            elif node.right is not None:
                queue.append(TreeNode(-1))

            # if node.left is None and node.right is not None:
            #     print("null")
            # if node.right is None and node.left is not None:
            #     print("null")

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
            elif node.left is not None:
                queue.append(TreeNode(-1))

    def printPreorder(self, root: TreeNode):
        if root is None:
            # print("null")
            return

        print(root.val),
        self.printPreorder(root.left),
        self.printPreorder(root.right)

    def printPreorder(self, root: TreeNode):
        if root is None:
            # print("null")
            return

        print(root.val),
        self.printPreorder(root.left),
        self.printPreorder(root.right)

    def printPostorder(self, root: TreeNode):
        if root is None:
            return

        self.printPostorder(root.left),
        self.printPostorder(root.right),
        print(root.val)

    def printInorder(self, root: TreeNode):
        if root is None:
            # print("null")
            return
        self.printInorder(root.left)
        print(root.val),
        self.printInorder(root.right)


s = Solution();
print(s.bstFromPreorder([8, 5, 1, 7, 10, 12]))
# print(s.bstFromPreorder([10, 5, 1, 7, 40, 50]))
