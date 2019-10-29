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
    def sol1(self, head) :
        if not head or not head.next : return head
        dummy = prev = ListNode(0)
        dummy.next = head
        while prev.next and prev.next.next : 
            temp = prev.next.next
            prev.next.next = temp.next
            temp.next = prev.next
            prev.next = temp
            prev = temp.next
        return dummy.next

    def sol2(self, head) :
        if not head or not head.next : return head
        temp = head.next
        head.next = self.sol2(head.next.next)
        temp.next = head
        return temp

    def swapPairs(self, head: ListNode) -> ListNode:
        # return self.sol1(head)
        return self.sol2(head)
            


        
# @lc code=end

