#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.sol1(root)

    def sol1(self, root) :
        mem = dict()
        return self.dfs(mem, root)

    def dfs(self, mem, root) :
        if not root : return 0
        if root in mem : return mem[root]
        val = 0
        if root.left :
            val += self.dfs(mem, root.left.left) + self.dfs(mem, root.left.right)
        if root.right :
            val += self.dfs(mem, root.right.left) + self.dfs(mem, root.right.right)
        
        val = max(root.val + val, self.dfs(mem, root.left) + self.dfs(mem, root.right))
        mem[root] = val
        return val

        



        
# @lc code=end

