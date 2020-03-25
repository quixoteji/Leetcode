#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n == 0: return head 
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, dummy
        for i in range(n) :
            p1 = p1.next
        while p1.next :
            p1, p2 = p1.next, p2.next
        
        p2.next = p2.next.next
        return dummy.next

        
# @lc code=end

