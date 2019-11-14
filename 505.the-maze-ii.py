#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        ans = []
        s , t = start, destination
        left, right, up, down = [0, -1], [0, 1], [-1, 0], [1, 0]
        directions = [left, right, up, down]
        queue = []
        queue.append([s[0], s[1], 0])
        visited[s[0]][s[1]] = True
        while queue :
            s = queue.pop(0)
            if s[0] == t[0] and s[1] == t[1] : ans.append(s[2])
            for dirt in directions :
                s_x, s_y, val  = s[0] + dirt[0], s[1] + dirt[1], s[2] + 1
                while s_x >= 0 and s_x < len(maze) and s_y >= 0 and s_y < len(maze[0]) and maze[s_x][s_y] == 0 :
                    s_x, s_y, val = s_x + dirt[0], s_y + dirt[1], val + 1
                if not visited[s_x - dirt[0]][s_y - dirt[1]] :
                    visited[s_x - dirt[0]][s_y - dirt[1]] = True
                    queue.append([s_x - dirt[0], s_y - dirt[1], val - 1])
        print(ans)
        return min(ans) if ans else -1
                
# @lc code=end

