#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return self.sol2(timeSeries, duration)

    def sol1(self, timeSeries, duration) :
        sections = []
        for times in timeSeries :
            sections.append([times, times + duration])
        sections.sort(key = lambda x : x[0])
        ans = []
        for section in sections:
            if ans and ans[-1][0] <= section[0] <= ans[-1][1] :
                ans[-1] = [ans[-1][0], max(ans[-1][1], section[1])]
            else :
                ans.append(section)
        return sum([s[1] - s[0] for s in ans])

    def sol2(self, timeSeries, duration) :
        if not timeSeries : return 0
        ans = 0
        for i in range(len(timeSeries) - 1): 
            ans += duration if timeSeries[i] + duration < timeSeries[i + 1] else timeSeries[i + 1] - timeSeries[i]
        return ans + duration
            



        
# @lc code=end

