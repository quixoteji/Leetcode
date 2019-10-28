#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev, curr, n = [], [], 1
        while n <= rowIndex + 1:
            curr = [1 for i in range(n)]
            if n > 2 :
                for i in range(1, n - 1) : curr[i] = prev[i - 1] + prev[i]
            prev = curr
            n += 1
        return curr
        

        
# @lc code=end

