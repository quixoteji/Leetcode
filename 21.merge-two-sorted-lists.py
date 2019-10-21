#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = head = ListNode(0)
        while l1 or l2:
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')
            dummy.next = l1 if val1 < val2 else l2
            dummy = dummy.next
            (l1, l2) = (l1.next, l2) if val1 < val2 else (l1, l2.next)
        return head.next

        
# @lc code=end

