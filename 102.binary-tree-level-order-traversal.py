#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root : return ans
        stack = []
        stack.append(root)
        while stack :
            level = []
            nextlevel = []
            for node in stack :
                level.append(node.val)
                if node.left : nextlevel.append(node.left)
                if node.right : nextlevel.append(node.right)
            ans.append(level[:])
            stack = nextlevel[:]
        return ans
            



        
# @lc code=end

