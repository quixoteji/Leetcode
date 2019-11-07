#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ranks = []
        ans = ['' for _ in range(len(nums))]
        for i, v in enumerate(nums) :
            ranks.append([i, v])
        ranks = sorted(ranks, key = lambda x : x[1])
        for i in range(len(ranks)) :
            ans[ranks[i][0]] = str(ranks[i][1] + 1)
        for s in ans :
            if s == '1' : s = "Gold Medal"
            if s == '2' : s = "Silver Medal"
            if s == '3' : s = "Bronze Medal"
        return ans
        
# @lc code=end

