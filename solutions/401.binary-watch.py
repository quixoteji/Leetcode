#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:

    def dfs(self, ans, s, ones, num) :
        if ones > num : return
        if len(s) > 10 : return
        if ones == num and len(s) == 10 :
            hours = int(s[0:4], 2)
            minutes = int(s[4:], 2)
            if hours > 11 or minutes > 59 : return
            s_hours = str(hours) if hours != 0 else '0'
            s_minutes = str(minutes) if minutes > 9 else '0' + str(minutes)
            ans.append(s_hours + ':' + s_minutes)
            return
        self.dfs(ans, s + '0', ones, num)
        self.dfs(ans, s + '1', ones + 1, num)

    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        s = ''
        ones = 0
        self.dfs(ans, s, ones, num)
        return ans
# @lc code=end

