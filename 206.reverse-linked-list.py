#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next : return head
        dummy = prev = ListNode(0)
        dummy.next = head
        while head :
            nextNode = head.next
            dummy.next = nextNode
            head = head.next
            
        return dummy.next
        
# @lc code=end

