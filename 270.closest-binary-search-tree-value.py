#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bfs(self, root, target) :
        if not root : return None
        val = float('inf')
        queue = []
        queue.append(root)
        while queue :
            nextlevel = []
            for node in queue :
                val = node.val if abs(node.val - target) < abs(target - val) else val
                if node.right : nextlevel.append(node.right)
                if node.left : nextlevel.append(node.left)
            queue = nextlevel[:]
        return val

    def dfs(self, root, res) :
        if not root : return 
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)


    def closestValue(self, root: TreeNode, target: float) -> int:
        res = []
        self.dfs(root, res)
        return min(res, key = lambda x : abs(x - target))
        
        
# @lc code=end

