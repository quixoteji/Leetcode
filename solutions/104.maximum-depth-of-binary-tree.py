#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sol1(self, root):
        ans = 0
        if not root : return ans
        level = []
        level.append(root)
        while level :
            nextlevel = []
            ans += 1
            for node in level :
                if node.left : nextlevel.append(node.left)
                if node.right : nextlevel.append(node.right)
            level = nextlevel[:]
        return ans

    def sol2(self, root, val) :
        if not root : return val
        return max(self.sol2(root.left, val + 1), self.sol2(root.right, val + 1))

    def maxDepth(self, root: TreeNode) -> int:
        # return self.sol1(root)
        return self.sol2(root, 0)
        
# @lc code=end

