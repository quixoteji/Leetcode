#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    # topological sort
    # 0 : unknown 1 : visiting 2 : visited

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.sol1(n, edges)
        
    # Solution 1 : dfs
    def sol1(self, n, edges) :
        # 0: not visiting
        # 1 : visiting
        # 2 : visited
        state = [0 for i in range(n)]
        graph = [list() for i in range(n)]
        for edge in edges :
            graph[edge[0]].append(edge[1])

        for node in range(n) :
            if self.dfs(graph, state, node) : return False
        return True

    def dfs(self, graph, state, node) :
        if state[node] == 1 : return True
        if state[node] == 2 : return False
        state[node] = 1
        for n in graph[node] :
            if self.dfs(graph, state, n) : return True
        state[node] = 2
        return False




# @lc code=end

