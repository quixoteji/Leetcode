#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def hashtable(self, matrix) :
        if len(matrix) < 1 or len(matrix[0]) < 1 : return
        ihtable, jhtable = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    ihtable.add(i)
                    jhtable.add(j)
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if i in ihtable or j in jhtable :
                    matrix[i][j] = 0
        return
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.hashtable(matrix)
        
# @lc code=end

