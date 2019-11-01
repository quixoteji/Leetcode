#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        while l <= r :
            m = l + (r - l) // 2
            if citations[m] >= m :
                l = m
            else :
                r = m - 1
        return l+1

# @lc code=end

