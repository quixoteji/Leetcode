#
# @lc app=leetcode id=335 lang=python3
#
# [335] Self Crossing
#

# @lc code=start
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        return self.sol1(x)

    def sol1(self, x) :
        if len(x) < 4 : return False
        for pos in range(3, len(x)) :
            if x[pos - 1] <= x[pos - 3] and x[pos] >= x [pos - 2] :
                return True
            if pos >= 4 and x[pos - 1] == x[pos - 3] and x[pos] + x[pos - 4] == x[pos - 2]: 
                return True
            if pos >= 5 and x[pos-1] <= x[pos-3] and x[pos-3] <= x[pos-1] + x[pos-5] and x[pos] + x[pos-4] >= x[pos-2] and x[pos-4] <= x[pos-2]:
                return True
        return False
        
# @lc code=end

