#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        return self.sol1(head, m, n)

    def sol1(self, head, m, n) :
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m-1) : prev = prev.next
        curr = prev.next
        for i in range(m, n) :
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
        
# @lc code=end

