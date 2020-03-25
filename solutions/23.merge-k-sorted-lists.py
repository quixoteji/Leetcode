#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Node():
    def __init__(self, node) :
        self.val = node.val
        self.node = node
    def __lt__(self, other) :
        return self.val < other.val

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        dummy = head = ListNode(0)
        for node in lists:
            if node :
                heapq.heappush(heap, Node(node))
        
        while heap :
            node = heapq.heappop(heap).node
            if node.next :
                heapq.heappush(heap, Node(node.next))
            dummy.next = node
            dummy = dummy.next

        return head.next



# @lc code=end

