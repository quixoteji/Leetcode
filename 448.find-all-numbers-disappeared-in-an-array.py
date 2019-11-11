#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums :
            idx = abs(num) - 1
            nums[idx] = -1 * nums[idx] if nums[idx] > 0 else nums[idx]
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
# @lc code=end

