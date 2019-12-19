class Solution:
    def shortestPath(self, grid, k):
        # State (x, y, k) -> k is the number of obstacles
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        m, n = len(grid), len(grid[0])
        # seen[x][y] = min obstacles to reach (x, y)
        seen = [[float('inf') for _ in range(n)] for _ in range(m)]
        queue = []
        steps = 0
        queue.append((0, 0, 0))
        while queue:
            l = len(queue)
            for i in range(l) :
                x, y, o = queue.pop(0)
                if x == m - 1 and y == n - 1 : return steps
                for (dx, dy) in dirs :
                    cx, cy = x + dx, y + dy
                    if cx < 0 or cy < 0 or cx > m - 1 or cy > n - 1 : continue
                    co = o + grid[cx][cy]
                    if co > seen[cx][cy] or co > k : continue
                    seen[cx][cy] = co
                    queue.append((cx, cy, co))
            steps += 1
        return -1
                

A = Solution()
print(A.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))


