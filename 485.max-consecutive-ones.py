#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.insert(0,0)
        nums.append(0)
        i, j = 0, 0
        ans = 0
        while i < len(nums) and j < len(nums) :
            if nums[j] == 1 :
                while j + 1 < len(nums) and nums[j+1] == 1 : j += 1
                ans = max(ans, j - i)
                i = j
            else :
                i += 1
            j += 1
        return ans
        
# @lc code=end

