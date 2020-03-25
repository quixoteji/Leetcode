#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def dfs(self, root, ans) :
        if not root : return
        for child in root.children :
            self.dfs(child, ans)
        ans.append(root.val)
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root : return ans
        self.dfs(root, ans)
        return ans
# @lc code=end

