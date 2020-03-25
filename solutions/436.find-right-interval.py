#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index, d , ans= dict(), dict(),[]
        for i,[start, end] in enumerate(intervals):
            index[(start, end)] = i
            d[start] = end
        m, so = max(d.keys()), sorted(d.keys())
        for start, end in intervals:
            if end > m: ans.append(-1)
            else:
                ind = bisect.bisect_left(so, end)
                ans.append(index[(so[ind], d[so[ind]])])
        return ans

        
# @lc code=end

