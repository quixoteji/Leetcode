#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head : return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head
        while curr :
            while curr.next and curr.val == curr.next.val :
                curr = curr.next
            else :
                prev, curr = prev.next, curr.next
        return dummy.next
        
# @lc code=end

