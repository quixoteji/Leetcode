#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return self.sol1(head)

    def sol1(self, head) :
        if not head or not head.next : return head
        dummy1, dummy2 = ListNode(0), ListNode(0)
        odd, even = dummy1, dummy2

        while head :
            odd.next = head
            odd, head = odd.next, head.next, 
            if head : 
                even.next = head
                even, head = even.next, head.next
        
        odd.next = dummy2.next
        even.next = None
        return dummy1.next
            

            
        
# @lc code=end

