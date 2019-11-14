#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head) :
        prev, curr = None, head
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        return prev
    def plusOne(self, head: ListNode) -> ListNode:
        if not head : return head
        dummy = head = self.reverse(head)
        carry = 1
        while head :
            head.val = (head.val + carry) % 10
            carry = (head.val + carry) // 10
            head = head.next
        if carry : head = 
        return self.reverse(dummy)
        
# @lc code=end

