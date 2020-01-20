#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.sol1(s, t)

    # Solution 1 : iteration
    def sol1(self, s, t) :
        if not s or not t : return 0
        if s == t : return 1
        ct = collections.Counter(t)
        cs = collections.Counter(s)
        for key in ct : 
            if ct[key] > cs[key] : return 0
        for i in range()
        
        

        
# @lc code=end

