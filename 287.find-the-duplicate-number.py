#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.sol1(nums)

    def sol1(self, nums) : 
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast : break
        fast = 0 
        while fast != slow :
            slow = nums[slow]
            fast = nums[fast]
        return slow
            
        
# @lc code=end

