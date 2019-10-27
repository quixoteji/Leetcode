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
        if not head or not head.next: return head
        dummy = prev = ListNode(0)
        dummy.next = head
        while prev and prev.next :
            temp = prev.next.next
            prev.next.next = temp.next
            temp.next = prev.next
            prev.next = temp
            prev = prev.next.next
        
        return dummy.next
            


        
# @lc code=end

