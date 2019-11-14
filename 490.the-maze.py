#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#

# @lc code=start
class Solution:
    def dfs(self, maze, s, t, visited) :
        if visited[s[0]][s[1]] : return False
        if s[0] == t[0] and s[1] == t[1] : return True
        visited[s[0]][s[1]] = True
        r, l, u, d = s[1] + 1, s[1] - 1, s[0] - 1, s[0] + 1   
        length, width = len(maze), len(maze[0])
        # Right
        while r < width and maze[s[0]][r] == 0 :
            r += 1
        if self.dfs(maze, [s[0], r - 1], t, visited) : 
            return True
        # Left
        while l >= 0 and maze[s[0]][l] == 0 :
            l -= 1
        if self.dfs(maze, [s[0], l + 1], t, visited) : 
            return True
        # Up
        while u >= 0 and maze[u][s[1]] == 0 :
            u -= 1
        if self.dfs(maze, [u + 1, s[1]], t, visited) : 
            return True
        # Down
        while d < length and maze[d][s[1]] == 0 :
            d += 1
        if self.dfs(maze, [d - 1, s[1]], t, visited) : 
            return True
        return False

    def bfs(self, maze, s, t, visited) :
        left, right, up, down = [0, -1], [0, 1], [-1, 0], [1, 0]
        directions = [left, right, up, down]
        queue = []
        queue.append(s)
        visited[s[0]][s[1]] = True
        while queue :
            s = queue.pop(0)
            if s[0] == t[0] and s[1] == t[1] : return True
            for dirt in directions :
                s_x, s_y = s[0] + dirt[0], s[1] + dirt[1]
                while s_x >= 0 and s_x < len(maze) and s_y >= 0 and s_y < len(maze[0]) and maze[s_x][s_y] == 0 :
                    s_x, s_y = s_x + dirt[0], s_y + dirt[1]
                if not visited[s_x - dirt[0]][s_y - dirt[1]] :
                    visited[s_x - dirt[0]][s_y - dirt[1]] = True
                    queue.append([s_x - dirt[0], s_y - dirt[1]])
        return False
                




    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # return self.dfs(maze, start, destination, [[False for _ in range(len(maze[0]))] for _ in range(len(maze))])
        return self.bfs(maze, start, destination, [[False for _ in range(len(maze[0]))] for _ in range(len(maze))])


        
# @lc code=end

