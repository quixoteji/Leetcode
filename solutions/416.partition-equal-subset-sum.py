#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.sol1(nums) 


    def sol1(self, nums) :
        if not nums or sum(nums) % 2: return False
        target = sum(nums) // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums :
            for i in range(target, num - 1, -1) :
                dp[i] = dp[i] or dp[i - num]
        return dp[target]


        
# @lc code=end

