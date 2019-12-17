#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        if low < 10 or low >= high: return ans
        for i in range(1, 10) :
            n = i
            for j in range(i + 1, 10) :
                n = n * 10 + j 
                if low <= n <= high: ans.append(n)
        return sorted(ans)
        
# @lc code=end

