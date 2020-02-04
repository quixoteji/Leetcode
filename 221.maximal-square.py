#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.sol1(matrix)

    def sol1(self, matrix) :
        if not matrix or not matrix[0] : return 0
        maxVal = 0
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == '1' :
                    if i > 0 and j > 0 :
                        matrix[i][j] = min(int(matrix[i - 1][j - 1]), int(matrix[i - 1][j]), int(matrix[i][j - 1])) + 1
                    elif i == 0 or j == 0 : 
                        matrix[i][j] = 1
                    
                    maxVal = max(matrix[i][j], maxVal)
        return maxVal * maxVal


        
# @lc code=end

