#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        return self.sol1(matrix, k)

    def sol1(self, matrix, k) :
        if k == 0 : return -1
        if not matrix or not matrix[0] or k < 0 : return -1
        m, n = len(matrix), len(matrix[0])
        _sum = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m) :
            for j in range(n) :
                temp = matrix[i][j]
                if i > 0 : temp += _sum[i - 1][j]
                if j > 0 : temp += _sum[i][j - 1]
                if i > 0 and j > 0 : temp -= _sum[i - 1][j - 1]
                _sum[i][j] = temp

                for r in range(i + 1) :
                    for c in range(j + 1) :
                        d = _sum[i][j]
                        if (r > 0) : d -= _sum[r - 1][j]
                        if (c > 0) : d -= _sum[i][c - 1]
                        if (r > 0 and c > 0) : d += _sum[r - 1][c - 1]
                        if d == k : return k
                        if d < k : ans = max(ans, d)
        return ans
        
# @lc code=end

