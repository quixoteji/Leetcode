#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums : return []
        nums.sort()
        dp = [list() for _ in range(len(nums))]
        dp[0] = [nums[0]]

        for i in range(1, len(nums)) :
            curr = nums[i]
            maxSet = []
            for j in range(i) :
                if curr % nums[j] == 0 :
                    localSet = dp[j][:]
                    if len(localSet) > len(maxSet) :
                        maxSet = localSet
            maxSet.append(nums[i])
            dp[i] = maxSet[:]
        
        ans = []
        for localSet in dp :
            if len(localSet) > len(ans) :
                ans = localSet
        return ans

# @lc code=end

