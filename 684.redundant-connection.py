#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class UFset :
    def __init__(self, n) :
        self._parents = [i for i in range(n+1)]
        self._ranks = [1 for i in range(n+1)]
    def union(self, x, y) :
        px, py = self.find(x), self.find(y)
        if px == py : return False
        if self._ranks[px] < self._ranks[py] : 
            self._parents[px] = py
        elif self._ranks[px] > self._ranks[py] :
            self._parents[px] = px
        else :
            self._parents[py] = px
            self._ranks[px] += 1
        return True
    def find(self, x) :
        if x != self._parents[x] : 
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        _ufset = UFset(len(edges))
        for edge in edges :
            if not _ufset.union(edge[0], edge[1]):
                return edge
        return []
        
# @lc code=end

