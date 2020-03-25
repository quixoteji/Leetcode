#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next : return head
        dummy = ListNode(0)
        curr = dummy
        while head :
            temp = head.next
            curr = dummy
            while curr.next and curr.next.val <= head.val : curr = curr.next
            head.next = curr.next
            curr.next = head
            head = temp
        return dummy.next
        

        
# @lc code=end

