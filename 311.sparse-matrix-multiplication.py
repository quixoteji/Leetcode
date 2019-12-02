#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
class Solution:
    # Solution 1 : matrix multiplication
    def sol1(self, A, B) :
        rows, cols = len(A), len(B[0])
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows) :
            for c in range(cols) :
                a, b = A[r], B[:][c]
                
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return self.sol1(A, B)

# @lc code=end

