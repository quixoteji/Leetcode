#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3 : return sum(nums)
        
        nums.sort()
        ans = sum(nums[:3])
        for i, v in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i] : continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                diff = abs(v + nums[l] + nums[r] - target)
                _diff = abs(ans - target)
                if diff < _diff :
                    ans = v + nums[l] + nums[r]
                
                if v + nums[l] + nums[r] == target :
                    return target
                elif v + nums[l] + nums[r] < target :
                    l += 1
                else :
                    r -= 1
        return ans  
    
# @lc code=end

