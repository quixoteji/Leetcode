#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        return self.sol1(m, n, positions)

    def sol1(self, m, n, positions) :
        def find(x):
            if ps[x] != x:
                ps[x] = find(ps[x])
            return ps[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                ps[py] = px
                return -1
            return 0
                
        ps, res, count = {}, [], 0
        grid = [[0] * n for _ in range(m)]
        for i, j in positions:
            if grid[i][j] == 1:
                res += [count]
                continue
            ps[(i, j)] = (i, j)
            grid[i][j] = 1
            count += 1
            for di, dj in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == 1:
                    count += union((i, j), (i+di, j+dj))
            
            res += [count]
        
        return res

# @lc code=end

