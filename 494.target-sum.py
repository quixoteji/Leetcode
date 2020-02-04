#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.sol2(nums, S)

    def sol1(self, nums, S) :
        if sum(nums) < S or -1 * sum(nums) > S: return 0
        ans = []
        self.dfs(ans, 0, 0, nums, S)
        return len(ans)

    def dfs(self, ans, curr, idx, nums, S) :
        if idx == len(nums) :
            if curr == S : ans.append(curr)
            return
        self.dfs(ans, curr - nums[idx], idx + 1, nums, S)
        self.dfs(ans, curr + nums[idx], idx + 1, nums, S)

    def sol2(self, nums, S) :
        if not nums : return 0
        _sum = collections.defaultdict(int)
        _sum[nums[0]] += 1
        _sum[-nums[0]] += 1
        for i in range(1, len(nums)) :
            temp = collections.defaultdict(int)
            for d in _sum :
                temp[d + nums[i]] = temp[d + nums[i]] + _sum[d]
                temp[d - nums[i]] = temp[d - nums[i]] + _sum[d]
            _sum = temp
        return _sum[S]  
        
        
# @lc code=end

