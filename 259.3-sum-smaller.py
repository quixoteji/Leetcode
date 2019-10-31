#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start
class Solution:
    def sol1(self, nums, target) :
        res, n = 0, len(nums)
        for i in range(n) :
            for j in range(i + 1, n) :
                for k in range(j + 1, n) :
                    if nums[i] + nums[j] + nums[k] < target : res += 1
        return res

    def sol2(self, nums, target) :
        res = 0
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r :
                if nums[l] + nums[r] + nums[i] < target : 
                    res += r - l                    
                    l += 1
                else :
                    r -= 1
        return res

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        return self.sol1(nums, target)
        
# @lc code=end

