#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        min_index, max_index = len(temp), 0
        for i in range(len(temp)):
            if temp[i] != nums[i] : 
                min_index = min(min_index, i)
                max_index = max(max_index, i)
        ans = max_index - min_index + 1 
        return ans if ans > 0 else 0
        
# @lc code=end

