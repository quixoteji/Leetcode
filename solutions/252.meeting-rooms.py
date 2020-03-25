#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(len(intervals)) :
            if i > 0 and intervals[i][0] < intervals[i - 1][1] : return False
        return True
        
# @lc code=end

