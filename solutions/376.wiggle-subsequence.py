#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return self.sol1(nums)

    def sol1(self, nums) :
        if not nums : return 0
        t = []
        for i in range(1, len(nums)) :
            t.append(nums[i] - nums[i-1])
        p, n = 1, -1
        mxp = 1
        mxn = 1
        for i in range(len(t)):
            if t[i] * p > 0 :
                mxp, p = mxp + 1, p * -1
            if t[i] * n > 0 :
                mxn, n = mxn + 1, n * -1

        return max(mxp, mxn)
    
    def sol2(self, nums) :
        if not nums : return 0
        dp = [[1 for _ in nums] for _ in range(2)]
        p, n = 1, -1
        for i in range(1, len(nums)) :
            
            dp[0][i] = dp[0][i - 1] + ((nums[i] - nums[i -1]) * p > 1)
            dp[1][i] = dp[1][i - 1] + ((nums[i] - nums[i -1]) * n > 1)
        
            if nums[i] - nums[i - 1] * p > 1 : p *= -1
            if nums[i] - nums[i - 1] * n > 1 : n *= -1
        print(dp)
        return max(dp[0][-1], dp[1][-1])


        

        
# @lc code=end

