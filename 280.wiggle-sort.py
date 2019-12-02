#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#

# @lc code=start
class Solution:
    # Solution 1 : sort and swap -- O(nlog(n))
    def sol1(self, nums) :
        if len(nums) < 2 : return 
        nums.sort()
        idx = 1
        while idx + 1 < len(nums):
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
            idx += 2

    # Solution 2 : O(n)
    def sol2(self, nums) :
        if len(nums) < 2 : return
        for i in range(1, len(nums)) :
            if (i % 2 == 0 and nums[i] > nums[i - 1]) or (i % 2 == 1 and nums[i] < nums[i - 1]) :
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sol2(nums)
        
        

# @lc code=end

