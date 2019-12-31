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
        odd, even = ListNode(0), ListNode(0)
        dummy = head
        while dummy :
            odd = dummy
        return head
            
        
# @lc code=end

