#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    # topological sort
    # 0 : unknown 1 : visiting 2 : visited
    def dfs(self, n, state, graph) :
        if state[n] == 1 : return False
        if state[n] == 2 : return True
        state[n] = 1
        for node in graph[n] :
            if state[node] : return False

    def sol1(self, n, edges) :
        graph = [list() for _ in range(n)]
        state = [0 for _ in range(n)]
        for edge in edges :
            graph[edge[0]].append(edge[1])
        self.dfs(0, state, graph)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.sol1(n, edges)
        
# @lc code=end

