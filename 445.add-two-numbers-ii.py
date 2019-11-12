#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sol1(self, l1, l2) :
        stack1, stack2 = list(), list()
        while l1 : 
            stack1.append(l1.val)
            l1 = l1.next
        while l2 :
            stack2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(-1)
        carry = 0
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            node = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            temp = dummy.next
            node.next = temp
            dummy.next = node
        return dummy.next


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.sol1(l1, l2)

        
# @lc code=end

