#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans, n = [], 1
        while n <= numRows:
            curr = [1 for i in range(n)]
            if ans : curr[0] = curr[-1] = 1
            if n > 2 :
                for i in range(1, n - 1) : 
                    curr[i] = ans[n - 2][i - 1] + ans[n - 2][i]
            ans.append(curr[:])
            n += 1
        return ans
        
# @lc code=end

