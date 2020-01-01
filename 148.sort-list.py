#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.sol1(head)

    # Solution 1 : rebuilt
    def sol1(self, head) :
        if not head or not head.next: return head
        vals = []
        while head : 
            vals.append(head.val)
            head = head.next
        vals.sort()
        prev = dummy = ListNode(0)
        while vals :
            prev.next = ListNode(vals.pop(0))
            prev = prev.next
        return dummy.next
    
    # Solution 2 : mergesort
    



        
# @lc code=end

