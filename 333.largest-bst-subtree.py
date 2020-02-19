#
# @lc app=leetcode id=333 lang=python3
#
# [333] Largest BST Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        return self.solution1(root)

    ans = 0
    def solution1(self, root) :
        self.dfs(root)
        return self.ans

    def dfs(self, root) :
        if not root : return (0, float('inf'), float('-inf'))
        left_num, left_min, left_max = self.dfs(root.left)
        right_num, right_min, right_max = self.dfs(root.right)

        if left_num == -1 or right_num == -1 :
            return (-1, None, None)

        if root.val <= left_max or root.val >= right_min :
            return (-1, None, None)

        root_num = left_num + right_num + 1
        self.ans = max(self.ans, root_num)
        return (left_num + right_num + 1, min(root.val, left_min), max(root.val, right_max))

        
# @lc code=end

