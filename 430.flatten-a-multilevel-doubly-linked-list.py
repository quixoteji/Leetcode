#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        return self.sol1(head)
    
    # Solution 1 : iteration
    def sol1(self, head) :
        if not head : return head
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead
        stack = []
        stack.append(head)
        while stack :
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            if curr.next : stack.append(curr.next)
            if curr.child :
                stack.append(curr.child)
                curr.child = None
            
            prev = curr
        
        pseudoHead.next.prev = None
        return pseudoHead.next

    # Solution 2 : recurrsion
    def sol2(self, head) :
        if not head : return head
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)
        pseudoHead.next.prev = None
        return pseudoHead.next

    def flatten_dfs(self, prev, curr) :
        if not curr : return prev
        curr.prev = prev
        prev.next = curr
        tempNext = curr.next

        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        
        return self.flatten_dfs(tail, tempNext)



        
# @lc code=end

