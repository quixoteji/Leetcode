#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.sol2(nums)
    # Solution 1
    def sol1(self, nums):
        if len(nums) < 3: return len(nums)
        prev, curr, cnt = 0, 1, 1
        while curr < len(nums) :
            if nums[curr] == nums[prev] and cnt == 0 : curr += 1
            else :
                if nums[curr] == nums[prev] : cnt -= 1
                else : cnt = 1
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        return prev + 1

    # Solution 2 :
    def sol2(self, nums) :
        idx = 0
        for num in nums :
            if idx < 2 or num > nums[idx - 2] :
                nums[idx] = num
                idx += 1
        return idx              

        
# @lc code=end

