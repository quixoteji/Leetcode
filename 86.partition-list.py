#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        return self.sol1(head, x)

    def sol1(self, head, x) :
        if not head or not head.next : return head
        dummy, temp = ListNode(0), ListNode(0)
        second = temp
        prev, curr = dummy, head
        while curr :
            next = curr.next
            curr.next = None
            if curr.val < x : 
                prev.next = curr
                prev = prev.next
            else :
                temp.next = curr
                temp = temp.next
            curr = next
        prev.next = second.next
        return dummy.next
        
        
        
# @lc code=end

