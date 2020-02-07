import collections
import math

class Solution:
    def solve(self, m, n, positions) :
        if not m or not n : return 0
        sea = [[0 for _ in range(n)] for _ in range(m)]
        for pos in positions :
            sea[pos[0]][pos[1]] = 1

        ans = 0
        for i in range(m) :
            for j in range(n) :
                if sea[i][j] == 1 : 
                    ans += 1
                    self.dfs(sea, i, j)
        return ans

    def dfs(self, sea, i, j):
        m, n = len(sea), len(sea[0])
        sea[i][j] = 0
        d = [1, 0, -1, 0, 1]
        for x in range(4) :
            dx, dy = i + d[x], j + d[x + 1]
            if 0 <= dx < m and 0 <= dy < n and sea[dx][dy]:
                self.dfs(sea, dx, dy)
            
A = Solution()
print(A.solve(3,3,[[0,0],[0,1],[1,2],[2,1]]))
