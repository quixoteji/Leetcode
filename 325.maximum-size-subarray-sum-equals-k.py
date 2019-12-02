#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start
class Solution:
    # Solution 1 : hashmap
    def sol1(self, nums, k) :
        if not nums : return 0
        _sum = [sum(nums[:i]) for i in range(1, len(nums) + 1)]
        print(_sum)
        return 0

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        return self.sol1(nums, k)
        
# @lc code=end

