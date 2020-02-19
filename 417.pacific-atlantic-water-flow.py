#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix : return []
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]
        ans = []
        for i in range(m) :
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)
        for j in range(n) :
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)
        for i in range(m) :
            for j in range(n) :
                if p_visited[i][j] and a_visited[i][j] :
                    ans.append([i,j])
        return ans

    def dfs(self, matrix, i, j, visited, m, n):
        visited[i][j] = True
        for dir in self.directions :
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)   
# @lc code=end

