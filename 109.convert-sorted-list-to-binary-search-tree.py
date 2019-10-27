#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def listToArray(self, head) :
        nums = []
        if not head : return nums
        while head :
            nums.append(head.val)
            head = head.next
        return nums
        
    def arrayToBST(self, nums) :
        if not nums : return None
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        root.left = self.arrayToBST(nums[:idx])
        root.right = self.arrayToBST(nums[idx+1:])
        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.arrayToBST(self.listToArray(head))
        
        
# @lc code=end

