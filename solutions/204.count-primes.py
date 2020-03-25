#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        temp = [False, False] + [True for _ in range(n - 2)]
        for i in range(2, n) :
            if temp[i] : temp[i*i : n : i] = [False] * len(temp[i*i : n : i])
        return sum(temp)
                
        
# @lc code=end

