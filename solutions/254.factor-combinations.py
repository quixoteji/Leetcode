#
# @lc app=leetcode id=254 lang=python3
#
# [254] Factor Combinations
#

# @lc code=start
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        return self.sol1(n)

    def sol1(self, n) : 
        def dfs(n, i, curr, ans) :
            while i * i <= n :
                if n % i == 0 :
                    ans.append(curr + [i, n//i])
                    dfs(n//i, i, curr + [i], ans)
                i += 1
            return ans
        return dfs(n, 2, [], [])


        
# @lc code=end

