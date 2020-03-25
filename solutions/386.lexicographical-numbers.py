#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return self.sol1(n)

    def sol1(self, n) :
        ans = []
        for i in range(1, 10) :
            self.dfs(ans, i, n)
        return ans

    def dfs(self, ans, num, n) :
        if num > n : return 
        ans.append(num)
        for i in range(10) :
            self.dfs(ans, num * 10 + i, n)

        
# @lc code=end

