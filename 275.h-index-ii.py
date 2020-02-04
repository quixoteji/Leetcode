#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return self.sol1(citations)

    def sol1(self, citations) :
        _len = len(citations)
        l, r = 0, _len - 1
        while l <= r :
            mid = l + (r - l) // 2
            if citations[mid] == _len - mid : return _len - mid
            elif citations[mid] > _len - mid : r = mid - 1
            else : l = mid + 1
        return _len - l

# @lc code=end

