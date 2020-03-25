#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root : return []
        queue = []
        ans = []
        queue.append(root)
        while queue :
            l = len(queue)
            level = []
            for i in range(l) :
                node = queue.pop(0)
                level.append(node.val)
                for child in node.children :
                    queue.append(child)
            ans.append(level)
        return ans
# @lc code=end

