#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next : return head
        odd, even = head, head.next
        while head and head.next :
           odd, even = head, head.next
           odd = even.next
        odd.next = even.next
        return head
            
        
# @lc code=end

