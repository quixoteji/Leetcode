#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    # topological sort
    def dfs(self, n, start, graph) :
        if start[n] == 1 : return False
        if start[n] == 2 : return True
        start[n] = 1
        for node in graph[n] :
            if start[node] : return False




    def sol1(self, n, edges) :
        graph = [list() for _ in range(n)]
        state = [0 for _ in range(n)]
        for edge in edges :
            graph[edge[0]].append(edge[1])
        self.dfs(0, state, graph)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.sol1(n, edges)
        
# @lc code=end

