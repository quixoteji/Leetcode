#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
        prev, curr = None, head
        while curr :
            nextTemp = curr.next
            curr.next = prev
            prev, curr = curr, nextTemp    
        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        # if not head or not head.next : return head
        # dummy = ListNode(0)
        # dummy.next = head
        # while head and head.next :
        #     temp = head.next
        #     head.next = temp.next
        #     temp.next = dummy.next
        #     dummy.next = temp
        # return dummy.next
        return self.sol1(head)
        
# @lc code=end

