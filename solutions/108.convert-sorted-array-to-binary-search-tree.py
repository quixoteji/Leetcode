#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:  return None
        idx = len(nums)//2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[: idx])
        root.right = self.sortedArrayToBST(nums[idx + 1 :])
        return root
        
# @lc code=end

