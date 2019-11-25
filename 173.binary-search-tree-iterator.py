#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.vals = []
        self.root = root
        self.traverse(root)

    def traverse(self, root):
        if not root : return
        self.traverse(root.left)
        self.vals.append(root.val)
        self.traverse(root.right)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.vals.pop(0)


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.vals) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

