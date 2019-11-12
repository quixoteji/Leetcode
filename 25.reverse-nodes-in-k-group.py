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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1: return head
        
        out = ListNode(0)
        out.next = head
        ohead = out
        
        i = 0
        curr = head
        while curr:
            i += 1
            if i % k == 0:
                #otail can be None at the end. Set next to None so window can end when reversed
                otail, curr.next = curr.next, None
                #Reverse window and return new whead,wtail
                whead,wtail = self.reverse(ohead.next,curr)
                #Join the window back
                ohead.next, wtail.next = whead, otail
                #Move ohead forward one step and curr forward k steps
                ohead, curr = wtail, wtail.next
            else:
                curr = curr.next
        return out.next
    
    def reverse(self, start, end):
        pre, cur, tail = None, start, start
        while pre!=end:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail
        






        
# @lc code=end

