#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.sol2(intervals)

    # Solution 1 :
    def sol1(self, intervals) :
        if not intervals : return []
        intervals = sorted(intervals, key = lambda x : x[0])
        ans = []
        temp = intervals[0][:]
        for interval in intervals[1:] :
            if temp[1] >= interval[0] : 
                temp[1] = max(temp[1], interval[1])
            else : 
                ans.append(temp)
                temp = interval[:]
        ans.append(temp)
        return ans

    # Solution 2 :
    def sol2(self, intervals) :
        ans = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if not ans or interval[0] > ans[-1][1] : ans.append(interval)
            else : ans[-1][1] = max(interval[1], ans[-1][1])
        return ans
        
# @lc code=end

