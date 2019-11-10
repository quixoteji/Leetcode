#
# @lc app=leetcode id=558 lang=python3
#
# [558] Quad Tree Intersection
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if not quadTree1 and not quadTree2 : return None
        if quadTree1.isLeaf and quadTree2.isLeaf :
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        if quadTree1.isLeaf :
            return Node(True, True, None, None, None, None) if 
        
# @lc code=end

