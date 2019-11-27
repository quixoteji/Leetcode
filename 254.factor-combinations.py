#
# @lc app=leetcode id=254 lang=python3
#
# [254] Factor Combinations
#

# @lc code=start
class Solution:
    # backtrack
    def dfs(self, n, start, curr, ans) :
        if (n == 1) : 
            if len(curr) > 1 : 
                print(curr)
                ans.append(curr[:])
                return 
        for i in range(start, n) :
            if n % i == 0 :
                curr.append(i)
                self.dfs(n // i, i, curr, ans)
                curr.pop()
        return
    def sol1(self, n) :
        res = []
        curr = []
        self.dfs(n,  2, curr, res) 
        return res

    def getFactors(self, n: int) -> List[List[int]]:
        return self.sol1(n)

        
# @lc code=end

