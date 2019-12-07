#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.sol1(matrix)

    def sol1(self, matrix) :
        if not matrix : return []
        m, n = len(matrix), len(matrix[0])
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        seen = [[False for _ in range(n)] for _ in range(m)]
        ans = []
        i, j, d = 0, 0, 0
        for t in range(m * n):
            ans.append(matrix[i][j])
            seen[i][j] = True
            x = i + direction[d][0]
            y = j + direction[d][1]
            if 0 <= x < m and 0 <= y < n and not seen[x][y] :
                i, j = x, y
            else :
                d = (d + 1) % 4
                i = i + direction[d][0]
                j = j + direction[d][1]
        return ans


            
            



# @lc code=end

