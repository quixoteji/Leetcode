#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next : return head
        prev = dummy = ListNode(-1)
        dummy.next = head
        newhead = ListNode(-1)
        while prev.next :
            if prev.next >= x :
                prev.next 
        
# @lc code=end

