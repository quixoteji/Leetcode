#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.sol2(head)

    def sol1(self, head) :
        if not head or not head.next : return
        fast = slow = head
        while fast and fast.next : slow, fast = slow.next, fast.next.next
        mid = slow.next
        slow.next = None
        last, prev = mid, None
        while last :
            next = last.next
            last.next = prev
            prev = last
            last = next
        while head and prev :
            next = head.next
            head.next = prev
            prev = prev.next
            head.next.next = next
            head = next

    def sol2(self, head) :
        if not head or not head.next : return
        stack = []
        curr = head
        while curr :
            stack.append(curr)
            curr = curr.next
        cnt = (len(stack) - 1) // 2
        curr = head
        while cnt > 0 :
            node = stack.pop()
            next = curr.next
            curr.next = node
            node.next = next
            curr = next
            cnt -= 1
        curr = stack.pop()
        curr.next = None

# @lc code=end

