#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i] : continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                _sum = v + nums[l] + nums[r]
                if _sum == 0 :
                    ans.append([v, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l - 1] : l += 1
                    while l < r and nums[r] == nums[r + 1] : r -= 1
                else :
                    if _sum < 0 : l += 1
                    else : r -= 1
        return ans

        
# @lc code=end

