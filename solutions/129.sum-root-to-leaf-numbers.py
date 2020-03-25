#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root : return 0
        ans = []
        self.dfs(root, ans, '')
        return sum(ans)

    def dfs(self, root, ans, curr) :
        if not root.left and not root.right: 
            ans.append(int(curr + str(root.val)))
        if root.left : self.dfs(root.left, ans, curr + str(root.val))
        if root.right : self.dfs(root.right, ans, curr + str(root.val))

# @lc code=end

