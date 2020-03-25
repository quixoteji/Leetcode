#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
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
    def maxDepth(self, root: 'Node') -> int:
        if not root : return 0
        level = []
        level.append(root)
        queue = []
        queue.append(level)
        while level :
            next_level = []
            for node in level :
                for child in node.children :
                    next_level.append(child)
            queue.append(next_level)
            level = next_level
        return len(queue) - 1
# @lc code=end

