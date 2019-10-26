#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        i, j = 0, 0
        direct_1, direct_2 = -1, 0
        ans.append(matrix[i][j])
        for x in range(1, 2 * n - 1) :
            while i >= 0 and i < x and j >= 0 and j < n :
                i += direct_1
                j += direct_2


        
# @lc code=end

