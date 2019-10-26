#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root : return root
        if root.val == key : 
            if not root.left : return root.right
            if not root.right : return root.left
            temp = root.right
            root = root.left
            root.right = temp
            return root
        elif key > root.val : self.deleteNode(root.right, key)
        else : self.deleteNode(root.left, key)
        
# @lc code=end

