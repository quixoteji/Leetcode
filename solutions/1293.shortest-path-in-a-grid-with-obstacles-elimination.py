#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return self.bfs(grid, k)

    def bfs(self, grid, k) :
        m, n = len(grid), len(grid[0])
        q = collections.deque([[0,0,0]])
        visited = {(0,0) : 0}
        steps = 0
        while q :
            size = len(q)
            for _ in range(size) :
                r, c, obs = q.popleft()
                if obs > k : continue
                if r == m - 1 and c == n - 1 : return steps
                for r2, c2 in ([r+1,c], [r-1,c], [r,c+1], [r,c-1]) :
                    if 0 <=r2<=m-1 and 0 <=c2<=n-1 :
                        next_obs = obs + 1 if grid[r2][c2] == 1 else obs
                        if next_obs < visited.get((r2, c2), float('inf')) :
                            visited[(r2, c2)] = next_obs
                            q.append([r2, c2, next_obs])
            steps += 1
        return -1

    def bfs_time_limited(self, grid, k) :
        # State (x, y, k) -> k is the number of obstacles
        dirs = (0, 1, 0, -1, 0)
        m, n = len(grid), len(grid[0])
        # seen[x][y] = min obstacles to reach (x, y)
        seen = [[float('inf') for _ in range(n)] for _ in range(m)]
        queue = []
        steps = 0
        queue.append((0, 0, 0))
        while queue:
            l = len(queue)
            for i in range(l) :
                cx, cy, co = queue.pop(0)
                if cx == m - 1 and cy == n - 1 : return steps
                for i in range(4) :
                    x, y = cx + dirs[i], cy + dirs[i + 1]
                    if x < 0 or y < 0 or x >= m or y >= n : continue
                    o = co + grid[x][y]
                    if o > seen[x][y] or co > k : continue
                    seen[x][y] = co
                    queue.append((x, y, o))
            steps += 1
        return -1



        
# @lc code=end

