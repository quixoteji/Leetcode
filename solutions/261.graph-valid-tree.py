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
        graph = collections.defaultdict(list)
        for edge in edges:
            u,v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        visited = set([])
        if self.dfs(0, -1, graph, visited):
            return False
        if len(visited) != n:
            return False
        return True

    def dfs(self, node, parent, graph, visited):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                if self.dfs(nbr, node, graph, visited):
                    return True
            elif nbr in visited and nbr != parent:
                return True
        return False

    # UnionFind
    





# @lc code=end

