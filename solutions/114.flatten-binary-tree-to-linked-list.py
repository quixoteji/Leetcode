#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root : return None
        leftLast = self.flatten(root.left)
        rightLast = self.flatten(root.right)

        if leftLast :
            leftLast.right = root.right
            root.right = root.left
            root.left = None

        if rightLast : return rightLast
        if leftLast : return leftLast
        return root
        

        
# @lc code=end

