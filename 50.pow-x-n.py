#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.sol2(x, n)

    # Solution 1
    def sol1(self, x, n) :
        if n == 0 : return 1.0
        sign = 1 if n > 0 else 0
        n = abs(n)
        ans = 1
        while n > 0 :
            ans *= x
            n -= 1
        return ans if sign else 1/ans

    # Solution 2 
    def sol2(self, x, n) : 
        if n == 0 : return 1.0
        sign = 1 if n > 0 else 0
        n, ans = abs(n), 1
        while n > 0 :
            idx = 1
            temp = x 
            while idx * 2 < n :
                temp *= temp
                idx = idx * 2
            ans *= temp
            n -= idx
        return ans if sign else 1/ans



# @lc code=end

