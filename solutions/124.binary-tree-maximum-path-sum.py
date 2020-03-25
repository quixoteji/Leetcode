#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self) :
        self.ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.ans

    def traverse(self, root) :
        if not root : return 0
        left = max(self.traverse(root.left), 0)
        right = max(self.traverse(root.right), 0)
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val


    
        
        
# @lc code=end

