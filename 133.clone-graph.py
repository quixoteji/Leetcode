#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        head = Node(node.val, [])
        dummy = head
        stack = []
        stack.append(node) 
        while stack :
            l = len(stack)
            for i in range(l) :
                n = stack.pop()
                for nn in n.neighbors :
                    stack.append(nn)
                

        
# @lc code=end

