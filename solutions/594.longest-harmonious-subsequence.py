#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums: return 0
        counter = collections.Counter(nums)
        keys = sorted(counter.keys())
        ans = []
        for i in range(len(keys)) :
            if i > 0 and keys[i] - keys[i - 1] == 1:
                ans.append(counter[keys[i]] + counter[keys[i - 1]])
            
        return max(ans) if ans else 0

        
# @lc code=end

