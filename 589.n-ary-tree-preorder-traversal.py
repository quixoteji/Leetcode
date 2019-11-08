#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
        ans.append(root.val)
        for child in root.children :
            self.dfs(child, ans)

    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root : return []
        self.dfs(root, ans)
        return ans
        
# @lc code=end

