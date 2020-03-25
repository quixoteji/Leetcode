#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return self.sol1(intervals)

    def sol1(self, intervals) : 
        intervals.sort(key = lambda x : x[1])
        idx = 0
        ans = 0
        while idx < len(intervals) :
            right = intervals[idx][1]
            sec_idx = idx + 1
            while sec_idx < len(intervals) and intervals[sec_idx][0] < right :
                sec_idx += 1
            ans += sec_idx - idx - 1
            idx = sec_idx
        return ans


# @lc code=end

