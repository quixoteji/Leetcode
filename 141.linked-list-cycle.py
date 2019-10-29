#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next : return False
        slow = head.next
        fast = head.next.next
        while slow != fast :
            if not fast.next or not fast.next.next : return False
            slow = slow.next
            fast = fast.next.next
        return True

        
# @lc code=end

