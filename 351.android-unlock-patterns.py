#
# @lc app=leetcode id=351 lang=python3
#
# [351] Android Unlock Patterns
#

# @lc code=start
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        return self.sol2(m, n)

    def sol1(self, m, n) : 
        ans = 0
        visited = [False for _ in range(10)]

        jumps = [[0] * 10 for _ in range(10)]
        jumps[1][3] = jumps[3][1] = 2
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 8
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5

        ans += self.dfs(1, 1, 0, m, n, jumps, visited) * 4
        ans += self.dfs(2, 1, 0, m, n, jumps, visited) * 4
        ans += self.dfs(5, 1, 0, m, n, jumps, visited) 
        return ans

    def dfs(self, num, len, res, m, n, jumps, visited) :
        if len > m : res += 1
        if len > n : return res
        
        visited[num] = True
        for next in range(1, 10) :
            jump = jumps[num][next]
            if not visited[next] and (jump == 0 or visited[jump]) :
                res = self.dfs(next, len + 1, res, m, n, jumps, visited)
        visited[num] = False
        return res
    
    has_obstacle = {(1,3):2, (1,7):4, (1,9):5, (2,8):5, (3,7):5, (3,1):2, (3,9):6, (4,6):5, (6,4):5, (7,1):4, (7,3):5, (7,9):8, (8,2):5, (9,7):8, (9,3):6, (9,1):5}
    def sol2(self, m, n) :
        self.validPatterns = 0
        for num in range(1, 10):
            self.visited = set()
            self._getValidWays(num, 1, m, n)
        return self.validPatterns
    
    def _getValidWays(self, num, count, m, n):
		# consider the valid patterns only in length (m to n)
        if m <= count <= n:
            self.validPatterns += 1
		# after reaching path count 'n', we need not go on any further.
        if count == n:
            return
        
        self.visited.add(num)
        for nextNum in range(1, 10):
            if nextNum not in self.visited:
				# if a nextNum has an obstacle while starting from num, and is not visited previously, don't consider this path.
                if (num, nextNum) in self.has_obstacle and self.has_obstacle[(num, nextNum)] not in self.visited:
                    continue
                self._getValidWays(nextNum, count+1, m, n)
        self.visited.remove(num)
        
# @lc code=end

