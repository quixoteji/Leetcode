#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidLeft(self, root, val) :
        if not root : return True
        if root.val >= val : return False
        val = max(root.val, val)
        return self.isValidLeft(root.left, val) and self.isValidRight(root.right, val)

    def isValidRight(self, root, val) :
        if not root : return True
        if root.val <= val : return False
        return self.isValidLeft(root.left, root.val) and self.isValidRight(root.right, root.val)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root : return True
        return self.isValidLeft(root.left, root.val) and self.isValidRight(root.right, root.val)
        
        
# @lc code=end

