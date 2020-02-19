#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.sol1(root)

    def sol1(self, root) :
        if not root : return None
        queue = []
        queue.append(root)
        while queue :
            l = len(queue)
            ans = queue[0].val
            nextLevel = []
            for i in range(l) :
                node = queue.pop(0)
                if node.left : nextLevel.append(node.left)
                if node.right : nextLevel.append(node.right)
            if not nextLevel : return ans
            queue += nextLevel
        return ans



        
# @lc code=end

