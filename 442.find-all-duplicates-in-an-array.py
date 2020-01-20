#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return self.sol1(nums)

    def sol1(self, nums) :
        ans = []
        for i in range(len(nums)) :
            idx = abs(nums[i]) - 1
            if nums[idx] < 0 : ans.append(idx + 1)
            nums[idx] = -1 * nums[idx]
        return ans
     
# @lc code=end

