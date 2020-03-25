#
# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#

# @lc code=start
class union_find:
    def __init(self, n) :
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]
    def find(self, x) :
        if x != self._parents[x]:
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]
    def union(self, x, y) :
        px, py = self.find(x), self.find(y)
        if px == py : return False
        if self._ranks[px] < self._ranks[py] : self._parents[px] = py
        elif self._ranks[px] > self._ranks[py] : self._parents[py] = px
        else :
            self._parents[py] = px
            self._ranks[px] += 1

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        ufset = union_find(len(edges))
        for edge in edges :
            if not ufset.union(edge[0], edge[1]): return edge
        return []
        
# @lc code=end

