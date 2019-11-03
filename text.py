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
    def numIslands(self, grid) :
        # if len(grid) == 1 and grid[0][0] == "0" : return 0
        
        ufset = union_find(len(grid) * len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" : 
                    ufset.union(i, j)
        print(ufset._parents)
        hset = set()
        for parent in ufset._parents:
            hset.add(ufset.find(parent))
        return len(hset)

# -10,-3,0,5,9

A = Solution()
print(A.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))