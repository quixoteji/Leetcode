#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            dummy.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            dummy = dummy.next 
        return ans.next
        
# @lc code=end

