#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class UnionFind:
    def __init__(self, n) :
        self._parents = [i for i in range(n)]
        self._ranks = [1 for i in range(n)]

    def find(self, x):
        if x != self._parents[x] :
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def union(self, x, y) :
        px, py = self.find(x), self.find(y)
        if px == py : return False
        if self._ranks[px] > self._ranks[py] : self._parents[py] = px
        elif self._ranks[px] < self._ranks[py] : self._parents[px] = py
        else :
            self._parents[py] = px
            self._ranks[px] += 1
        return True

class Solution:
    # Solution 1 : Union Find
    def sol1(self, n, edges) :
        union_find = UnionFind(n)
        for edge in edges :
            union_find.union(edge[0], edge[1])
        for i in range(n) :
            union_find.find(i)
        return len(set(union_find._parents))

    # Solution 2 : Topological Sort
    def dfs(self, i, graph, state) :
        if not state[i] : return
        for node in graph[i] :
            state[i] = False 
            self.dfs(node, graph, state)

    def sol2(self, n, edges) :
        graph = [list() for _ in range(n)]
        state = [True for _ in range(n)]
        for edge in edges :
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        ans = 0
        for i in range(n) :
            if state[i] : 
                ans += 1
                self.dfs(i, graph, state)
        return ans

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return self.sol2(n, edges)
        
# @lc code=end

