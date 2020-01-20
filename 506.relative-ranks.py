#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums : return []
        ranks = []
        for i, v in enumerate(nums) : ranks.append((i, v))
        ranks = sorted(ranks, key = lambda x : x[1], reverse = True)
        ans = [0 for _ in nums]
        for i, (idx, rank) in enumerate(ranks): ans[idx] = i
        for i in range(len(ans)) :
            if ans[i] == 0: ans[i] = 'Gold Medal'
            elif ans[i] == 1: ans[i] = 'Silver Medal'
            elif ans[i] == 2: ans[i] = 'Bronze Medal'
            else : ans[i] = str(ans[i] + 1)
        return ans


        
# @lc code=end

