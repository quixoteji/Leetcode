#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(-1)
        dummy.next = head
        l = 0
        while head : head, l = head.next, l + 1
        for i in range(k % l) :
            prev, curr = dummy, dummy.next
            while curr.next : 
                prev, curr = prev.next, curr.next
            dummy.next, curr.next, prev.next = curr, dummy.next, None
        return dummy.next
        
# @lc code=end

