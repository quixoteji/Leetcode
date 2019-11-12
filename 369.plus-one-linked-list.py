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
    def sol1(self, head) :
        stack = list()
        while head : 
            stack.append(head.val)
            head = head.next
        head, carry = ListNode(0), 0
        while stack or carry :
            val = stack.pop()
            head.next = ()
    def plusOne(self, head: ListNode) -> ListNode:
        return self.sol1(head)
        
# @lc code=end

