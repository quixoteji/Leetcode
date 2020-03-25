#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root : return ans
        level = []
        level.append(root)
        while level :
            nextlevel = []
            temp = []
            for node in level :
                temp.append(node.val)
                if node.left : nextlevel.append(node.left)
                if node.right : nextlevel.append(node.right)
            ans.append(temp[:])
            level = nextlevel[:]
        return ans[::-1]
        
# @lc code=end

