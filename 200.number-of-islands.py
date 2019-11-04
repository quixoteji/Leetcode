#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class union_find:
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
        if self._ranks[px] > self._ranks[py] : self._parents[py] = px
        elif self._ranks[px] < self._ranks[py] : self._parents[px] = py
        else :
            self._parents[py] = px
            self._ranks[px] += 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid : return 0
        r, c = len(grid), len(grid[0])
        ufset = union_find(r * c)
        # print(ufset._parents)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" : 
                    if i+1 < r and grid[i+1][j] == "1" : ufset.union(i*c+j, (i+1)*c+j)
                    if i-1 >= 0 and grid[i-1][j] == "1" : ufset.union(i*c+j, (i-1)*c+j)
                    if j+1 < c and grid[i][j+1] == "1" : ufset.union(i*c+j, i*c+j+1)
                    if j-1 >=0 and grid[i][j-1] == "1" : ufset.union(i*c+j, i*c+j-1)
                if grid[i][j] == "0" :
                    ufset._parents[i*c+j] = -1
        print(ufset._parents)
        
        hset = set()
        for parent in ufset._parents:
            if parent != -1 :
                hset.add(ufset.find(parent))
        return len(hset)
# @lc code=end

