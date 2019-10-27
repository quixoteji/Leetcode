#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, root, d) :
        if root is None : return d
        return max(self.depth(root.left, d + 1), self.depth(root.right, d + 1))
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None : return True
        return abs(self.depth(root.left, 0) - self.depth(root.right, 0)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
# @lc code=end

