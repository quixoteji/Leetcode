#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        prev, curr = ListNode(0), head
        dummy, prev.next = prev, curr
        while curr :
            if curr.val == val: 
                prev.next = curr.next
                curr = curr.next
            else :
                prev, curr = prev.next, curr.next
        return dummy.next
# @lc code=end

