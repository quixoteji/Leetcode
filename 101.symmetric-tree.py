#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isequal(self, x, y):
        if not x or not y: 
            return x == y
        return x.val == y.val and self.isequal(x.left, y.right) and self.isequal(x.right, y.left)


    def isSymmetric(self, root: TreeNode) -> bool:
        if not root : return True
        else : return self.isequal(root.left, root.right)
        
# @lc code=end

