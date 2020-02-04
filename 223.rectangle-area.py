#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return self.sol1(A, B, C, D, E, F, G, H)

    def sol1(self, A, B, C, D, E, F, G, H) : 
        rec1 = (C - A) * (D - B)
        rec2 = (G - E) * (H - F)
        left = max(A,E)
        right = max(min(C,G), left)
        bottom = max(B,F)
        top = max(min(D,H), bottom)
        return rec1 + rec2 - (right - left) * (top - bottom)

        
# @lc code=end

