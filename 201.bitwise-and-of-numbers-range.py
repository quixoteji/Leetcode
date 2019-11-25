#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    # Solution1 : straightforward
    def sol1(self, a, b) :
        ans = a 
        for i in range(a + 1, b + 1) :
            ans &= i
            if ans == 0 : break
        return ans

    def sol2(self, m, n) :
        mask = 2 ** 31 - 1
        for i in range(31) :
            if m & mask == n & mask : break
            else : mask <<= 1
        return mask & m
            

        

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return self.sol2(m , n)
        
# @lc code=end

