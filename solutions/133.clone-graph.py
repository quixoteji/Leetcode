#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # return self.sol1(node)
        return self.sol2(node)

    # Solution 1 : BFS
    def sol1(self, node) :
        if not node : return node
        visited = dict()
        queue = [node]
        visited[node] = Node(node.val, [])
        while queue :
            n = queue.pop(0)
            for neighbor in n.neighbors :
                if neighbor not in visited :
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]

    # Solution 2 : DFS
    def sol2(self, node) :
        if not node : return node
        visited = dict()
        return self.dfs(node, visited)

    def dfs(self, node, visited) :
        if node in visited : return visited[node]
        clone_node = Node(node.val, [])
        visited[node] = clone_node
        if node.neighbors :
            clone_node.neighbors = [self.dfs(n, visited) for n in node.neighbors]
        return clone_node

        
# @lc code=end

