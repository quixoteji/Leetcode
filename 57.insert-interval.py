#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return self.sol1(intervals, newInterval)

    # Solution 1
    def sol1(self, intervals, newInterval) :
        ans = []
        n = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0] :
                intervals.insert(i, newInterval)
        if len(intervals) == n : intervals.append(newInterval) 
        print(intervals)
        for interval in intervals :
            if not ans or interval[0] > ans[-1][1] :
                ans.append(interval)
            else :
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


# @lc code=end

