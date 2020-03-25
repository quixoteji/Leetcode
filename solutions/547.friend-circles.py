#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class union_find :
    def __init__(self, n) :
        self._parents = [i for i in range(n)]
        self._ranks = [1 for i in range(n)]
    def find(self, x) :
        if x != self._parents[x] : 
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]
    def union(self, x, y) :
        px, py = self.find(x), self.find(y)
        if px == py : return False
        if self._ranks[px] > self._ranks[py] :
            self._parents[py] = px
        elif self._ranks[px] < self._ranks[py] :
            self._parents[px] = py
        else : 
            self._parents[py] = px
            self._ranks[px] += 1
        return True

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ufset = union_find(len(M)) 
        for i in range(len(M)) :
            for j in range(i+1, len(M)) :
                if M[i][j] : ufset.union(i, j)
        hset = set()
        for parent in ufset._parents :
            hset.add(ufset.find(parent))
        return len(hset)
        
# @lc code=end

