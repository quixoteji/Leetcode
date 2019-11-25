#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next : return head
        dummy = ListNode(0)
        prev, dummy.next = head, head
        while head :
            _next = head.next
            temp = dummy.next
            if head.val < temp.val :

        
# @lc code=end

