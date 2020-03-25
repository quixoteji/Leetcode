#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        distances = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        return self.search(maze, start, destination, distances)

    def search(self, maze, s, t, distances) :
        dirt = [1, 0, -1, 0, 1]
        queue = []
        queue.append(s)
        distances[s[0]][s[1]] = 0
        ans = []
        while queue :
            s = queue.pop(0)
            # print(s[0],s[1])
            dist = distances[s[0]][s[1]]
            for i in range(4) :
                s_d, s_x, s_y = dist, s[0] + dirt[i], s[1] + dirt[i+1]
                while 0 <= s_x < len(maze) and 0 <= s_y < len(maze[0]) and maze[s_x][s_y] == 0:
                    s_d, s_x, s_y = s_d + 1, s_x + dirt[i], s_y + dirt[i+1]
                s_d, s_x, s_y = s_d, s_x - dirt[i], s_y - dirt[i+1]
                if distances[s_x][s_y] > s_d :
                    distances[s_x][s_y] = s_d
                    if s_x != t[0] or s_y != t[1] : queue.append([s_x, s_y])
        # print(distances)
        
        return distances[t[0]][t[1]] if distances[t[0]][t[1]] != float('inf') else -1
# @lc code=end

