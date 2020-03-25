#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    first = None
    second = None
    prev = None

    def inorder(self, root) :
        if not root : return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val :
            if not self.first : self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder(root.right)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        print(self.first.val)
        print(self.second.val)
        self.first.val, self.second.val = self.second.val, self.first.val

        
# @lc code=end

