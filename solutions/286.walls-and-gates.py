#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.bfs_search(rooms)

    def bfs_search(self, rooms):
        if not rooms or not rooms[0] : return 
        m, n = len(rooms), len(rooms[0])
        direction = [1, 0, -1, 0, 1]
        INF = 2**31 - 1

        queue = []
        for i in range(m) :
            for j in range(n) :
                if rooms[i][j] == 0 : queue.append([i,j])

        while queue :
            l = len(queue)
            for nn in range(l) :
                i, j = queue.pop(0)
                for x in range(4) :
                    dx, dy = i + direction[x], j + direction[x + 1]
                    if 0 <= dx < m and 0 <= dy < n and rooms[dx][dy] == INF : 
                        queue.append([dx, dy])
                        rooms[dx][dy] = rooms[i][j] + 1
                                    


    def dfs_search(self, rooms) :
        if not rooms or not rooms[0] : return 
        INF = 2**31 - 1
        for i in range(len(rooms)) :
            for j in range(len(rooms[0])) :
                if rooms[i][j] == 0 : self.dfs(0, i, j, rooms)
        
    def dfs(self, level, i, j, rooms) :
        val = min(rooms[i][j], level)
        rooms[i][j] = -1
        d = [1, 0, -1, 0, 1]
        m, n = len(rooms), len(rooms[0])
        for x in range(4) :
            ix, jx = i + d[x], j + d[x + 1]
            if -1 < ix < m and -1 < jx < n and rooms[ix][jx] != -1 :
                self.dfs(level + 1, ix, jx, rooms)
        rooms[i][j] = val


        
# @lc code=end

