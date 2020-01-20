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
        nodes = [[] for _ in range(n)]
        for edge in edges : nodes[edge[0]].append(edge[1])

        for node in range(n) :
            if self.dfs(node) : continue



# @lc code=end

