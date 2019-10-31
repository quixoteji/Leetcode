#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, head):
        if head is None or head.next is None: return head
        

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head : return head
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        i = 0
        while head.next : 
            if i < k : 
                head = head.next
                k += 1
            else :
                temp = head.next
                head.next = None
                end = self.reverse(prev)
                end.next = temp
                head = temp
        return dummy.next



        
# @lc code=end

