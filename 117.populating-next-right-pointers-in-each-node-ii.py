#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root : return root
        queue = []
        queue.append(root)
        while queue :
            n = len(queue)
            for i in range(n) :
                t = queue.pop(0)
                if i < n - 1 : 
                    t.next = queue[0]
                if t.left : queue.append(t.left)
                if t.right : queue.append(t.right)
        return root
        
# @lc code=end

