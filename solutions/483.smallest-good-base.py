#
# @lc app=leetcode id=483 lang=python3
#
# [483] Smallest Good Base
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m = len(bin(n)) - 2
        while m > 0:
            low, high = 2, n - 1
            while low <= high :
                mid = (low + high) // 2
                res = (mid ** m - 1) // (mid - 1)
                if res == n: return str(mid)
                elif res < n: low = mid + 1
                else: high = mid - 1
            m -= 1
        return str(n)
        
# @lc code=end

