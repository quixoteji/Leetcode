#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, node) :
        prev, curr = None, node
        while curr :
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev

    def plusOne(self, head: ListNode) -> ListNode:
        if not head : return head
        node = self.reverse(head)
        prev = head = node
        carry = 1
        while node :
            prev = node
            carry, val = divmod(node.val + carry, 10)    
            node.val = val
            if carry == 0 : break
            node = node.next
        if carry : prev.next = ListNode(1)
        return self.reverse(head)
        
# @lc code=end

