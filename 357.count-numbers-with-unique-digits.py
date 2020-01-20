#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return self.sol2(n)

    # Solution 1 : dfs
    ans = 10
    def sol1(self, n) :
        if n == 0: return 1
        if n == 1 : return 10
        for i in range(1, 10) : self.dfs(str(i), n)
        return self.ans

    def dfs(self, s, n) :
        if len(s) == n : return
        for i in range(10) :
            if str(i) not in s : 
                self.ans += 1
                self.dfs(s + str(i), n)

    def sol2(self, n) :
        ans = 1 
        n = 9 if n > 9 else n
        for i in range(n) :
            term = 9
            for j in range(i) : 
                term *= 9 - j
            ans += term
        return ans 



        
# @lc code=end

