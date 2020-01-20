#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.sol3(nums, target)

    # Solution 1 : time limit exceeded
    def sol1(self, nums, target) :
        ans = list()
        nums.sort()
        self.dfs(ans, [], nums, target)
        return len(ans)

    def dfs(self, ans, curr, nums, target) :
        if sum(curr) > target : return
        if sum(curr) == target :
            ans.append(curr[:])
        for num in nums :
            curr.append(num)
            self.dfs(ans, curr, nums, target)
            curr.pop()

    # Solution 2 : 
    def sol2(self, nums, target) :
        mem = dict()
        return self.helper(nums, target, mem)
    
    def helper(self, nums, target, mem) :
        if target < 0 : return 0
        if target == 0 : return 1
        if target in mem : return mem[target]
        ans = 0
        for num in nums : ans += self.helper(nums, target - num, mem)
        mem[target] = ans
        return ans
        

    # Solution 3
    def sol3(self, nums, target) :
        dp = [1] + [0 for i in range(target)]
        for i in range(1, target + 1) :
            for num in nums :
                if i >= num : dp[i] += dp[i - num]
        # print(dp)
        return dp[-1]
# @lc code=end

