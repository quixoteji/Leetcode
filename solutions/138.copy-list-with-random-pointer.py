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
        return self.sol1(head)

    # Solution 1 :
    def sol1(self, head) :
        visited = dict()
        return self.dfs(head, visited)

    def dfs(self, head, visited) :
        if not head : return head
        if head in visited : return visited[head]
        node = Node(head.val, None, None)
        visited[head] = node
        node.next = self.dfs(head.next, visited)
        node.random = self.dfs(head.random, visited)
        return node
        

            

        
# @lc code=end

