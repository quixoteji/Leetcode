#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head : return True
        dummy = ListNode(0)
        dummy.next, k = head, 0
        while head :
            k, head = k + 1, head.next
        slow, fast, k, i = dummy, dummy, (k + 1) // 2, 0
        while fast :
            while i < k + 1 : fast, i = fast.next, i + 1
            
            if fast.val != slow.val : return False
            fast, slow = fast.next, slow.next
        return True



        
# @lc code=end

