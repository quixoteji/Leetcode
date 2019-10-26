#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head and not head.next: return head
        dummy = ListNode(0)
        dummy.next, prev, curr = head, dummy, head
        while curr.next :
            next = curr.next
            curr.next = next.next
            prev.next = next
            next.next = curr
            prev, curr = prev.next.next, curr.next

        return dummy.next
            


        
# @lc code=end

