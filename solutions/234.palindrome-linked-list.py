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
        fast = slow = head
        while fast.next and fast.next.next :
            slow, fast = slow.next, fast.next.next
        slow, fast, prev = head, slow.next, None
        while fast :
            temp = fast.next
            fast.next = prev
            fast, prev = temp, fast
        while prev :
            if prev.val == slow.val : prev, slow = prev.next, slow.next
            else : return False
        
        return True
        
# @lc code=end

