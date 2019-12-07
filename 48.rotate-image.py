#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2 : return
        layers = n // 2
        for layer in range(layers) :
            for i in range(layer, n - layer - 1) :
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - i - 1][layer]
                matrix[n - i - 1][layer] = matrix[n - 1 - layer][n - 1 - i]
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                matrix[i][n - 1 - layer] = temp
               
                


# @lc code=end

