#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#

# @lc code=start
class Solution:
    def search(self, maze, s, t, visited) :
        dirt = [1, 0, -1, 0, 1]
        queue = []
        queue.append(s)
        visited[s[0]][s[1]] = True
        while queue :
            s = queue.pop(0)
            if s[0] == t[0] and s[1] == t[1] : return True
            for i in range(4) :
                s_x, s_y = s[0] + dirt[i], s[1] + dirt[i+1]
                while s_x >= 0 and s_x < len(maze) and s_y >= 0 and s_y < len(maze[0]) and maze[s_x][s_y] == 0 :
                    s_x, s_y = s_x + dirt[i], s_y + dirt[i+1]
                if not visited[s_x - dirt[i]][s_y - dirt[i+1]] :
                    visited[s_x - dirt[i]][s_y - dirt[i+1]] = True
                    queue.append([s_x - dirt[i], s_y - dirt[i+1]])
        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        return self.search(maze, start, destination, visited)
        
# @lc code=end

