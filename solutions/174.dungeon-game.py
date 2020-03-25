#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
    # solution 1 for bfs
    def helper(self, ans, i, j, val, dungeon) :
        m, n = len(dungeon), len(dungeon[0])
        if i == m - 1 and j == n - 1 : 
            ans.append(val + dungeon[i][j])
            return
        if i < m - 1 :
            self.helper(ans, i + 1, j, val + dungeon[i][j], dungeon)
        if j < n - 1 :
            self.helper(ans, i, j + 1, val + dungeon[i][j], dungeon)
        

    def bfs(self, dungeon) :
        ans = []
        self.helper(ans, 0, 0, 0, dungeon)
        print(ans)
        return abs(max(ans)) + 1 if max(ans) < 0 else 1

    # solution 2 for dp
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        hp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        hp[m][n - 1] = hp[m - 1][n] = 1
        for i in range(m) : 
            for j in range(n) :
                r, c = m - 1 - i, n - 1 - j
                hp[r][c] = max(min(hp[r + 1][c], hp[r][c + 1]) - dungeon[r][c], 1)
        print(hp)
        return hp[0][0]
        
# @lc code=end

