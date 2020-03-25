#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.sol2(matrix)

    def sol2(self, matrix) :
        if not matrix or not matrix[0] : return []
        m, n = len(matrix), len(matrix[0])
        r, c, k = 0, 0, 0
        ans = [ 0 for _ in range(m * n)]
        dirs = [(-1, 1), (1, -1)]
        for i in range(m * n) :
            ans[i] = matrix[r][c]
            r, c = r + dirs[k][0], c + dirs[k][1]
            if r >= m : r, c, k = m - 1, c + 2, 1 - k
            if c >= n : r, c, k = r + 2, n - 1, 1 - k
            if r < 0 : r, k = 0, 1 - k
            if c < 0 : c, k = 0, 1 - k
        return ans

        



    def sol1(self, matrix) :
        if not matrix or not matrix[0] : return []
        if len(matrix) == 1 : return matrix[0]
        if len(matrix[0]) == 1 : return [x[0] for x in matrix]
        ans = []
        seen = set()
        m, n = len(matrix), len(matrix[0])
        for x in range(m + n - 1) :
            if x % 2 == 0 : i, j, direct = x, 0, (-1, 1)
            else : i, j, direct = 0, x, (1, -1)
            while i >= m or j >= n :
                if i >= m : i , j = i - 1, j + 1
                if j >= n : i , j = i + 1, j - 1
            while 0 <= i < m and 0 <= j < n :
                if (i, j) not in seen :
                    ans.append(matrix[i][j])
                    seen.add((i, j))
                i, j = i + direct[0], j + direct[1]
        return ans



        
# @lc code=end

