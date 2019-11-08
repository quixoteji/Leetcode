#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, num) :
        if not root : return 0
        root.left.val += root.val + self.dfs(root.right, root.val)
        root.val += 
         
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root : return root
        self.dfs(root, 0)
        return root
        
# @lc code=end

