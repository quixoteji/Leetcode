#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, ans) :
        if not root : return 
        if root.left : ans.append(root.left.val)
        self.dfs(root.left, ans)
        self.dfs(root.right, ans)
        

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root : return 0
        ans = []
        self.dfs(root, ans)
        return sum(ans)

        
# @lc code=end

