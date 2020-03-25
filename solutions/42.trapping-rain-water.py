#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        res = height[:]
        maxLeft, maxRight, hLen = 0, 0, len(height)
        for i in range(hLen) :
            maxLeft = left[i] = max(maxLeft, height[i])
            maxRight = right[hLen - 1 - i] = max(maxRight, height[hLen - 1 - i])
        for i in range(hLen) :
            res[i] = 0 if min(left[i], right[i]) - res[i] < 0 else min(left[i], right[i]) - res[i]
        return sum(res)

        
        
# @lc code=end

