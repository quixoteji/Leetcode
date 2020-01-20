#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#

# @lc code=start
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        return self.sol1(nums, a, b, c)

    def sol1(self, nums, a, b, c) : 
        ans = [0 for _ in nums]
        (idx, d) = (len(nums)- 1, -1) if a >= 0 else (0, 1)
        l, r = 0, len(nums) - 1
        nums = [a*(x**2)+b*x+c for x in nums]
        while l <= r :
            if a >= 0 :
                # print(idx)
                ans[idx] = nums[l] if nums[l] > nums[r] else nums[r]
                if nums[l] > nums[r] : l += 1
                else : r -= 1
                idx += d
            else :
                ans[idx] = nums[r] if nums[l] > nums[r] else nums[l]
                if nums[l] > nums[r] : r -=1 
                else : l += 1
                idx += d
        return ans
        
# @lc code=end

