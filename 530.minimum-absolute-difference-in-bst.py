#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root : return float('inf')
        ans = float('inf')
        if root.left :
            lmin = self.getMinimumDifference(root.left)
            ans = min(lmin, root.val - self.get_max_or_min(root.left, True))
        if root.right :
            rmin = self.getMinimumDifference(root.right)
            ans = min(ans, rmin, self.get_max_or_min(root.right, False) - root.val)
        return ans

    def get_max_or_min(self, root, _max = True):
        if _max :
            return self.get_max_or_min(root.right, True) if root.right else root.val
        else :
            return self.get_max_or_min(root.left, False) if root.left else root.val

# @lc code=end

