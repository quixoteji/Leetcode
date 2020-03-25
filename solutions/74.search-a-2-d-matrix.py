#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1 or len(matrix[0]) < 1 : return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        while low <= high :
            mid = (low + high) // 2
            value = matrix[mid // cols][mid % cols]
            if target == value : return True
            elif target > value : low = mid + 1
            else : high = mid - 1
        return False

        
# @lc code=end

