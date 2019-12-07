#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.sol1(n, k)

    # Solution 1 : dfs
    def sol1(self, n , k) :
        ans = []
        curr = ''
        self.dfs(ans, curr, n)
        return ans[k - 1]

    def dfs(self, ans, curr, n) :
        if len(curr) == n : 
            ans.append(curr)
            return
        

        
# @lc code=end

