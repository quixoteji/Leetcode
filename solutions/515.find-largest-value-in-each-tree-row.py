#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root : return None
        ans = []
        queue = []
        queue.append(root)
        while queue :
            l = len(queue)
            level = []
            for i in range(l) :
                node = queue.pop(0)
                level.append(node.val)
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
            ans.append(level)
        return [max(_) for _ in ans]
        
        
# @lc code=end

