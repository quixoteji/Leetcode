#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head : return head
        cloned_head = ListNode(head.val)
        cloned_head.next = head.next
        cloned_head.random = head.random
        dummy = cloned_head
        while dummy :
            node = dummy.next
            temp = ListNode(dummy.val)
            temp.
        
# @lc code=end

