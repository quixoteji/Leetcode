#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.sol1(root)

    # Solution 1 
    ans = 0
    def sol1(self, root) :
        if not root : return 0
        self.dfs(root, -100, 1)
        return self.ans

    def dfs(self, root, val, num) :
        if root.val == val + 1 : num += 1
        else : num = 1 
        self.ans = max(self.ans, num)
        if root.left : self.dfs(root.left, root.val, num)
        if root.right : self.dfs(root.right, root.val, num)

        
# @lc code=end

