#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def sol1(self, nums) :
        if len(nums) < 2 : return 0
        nums.sort()
        maxGap = 0
        for i in range(1, len(nums)) :
            maxGap = max(maxGap, nums[i] - nums[i - 1])
        return maxGap
    def bucket_sort(self, nums) :
        if len(nums) < 2 : return 0
        min_val, max_val = min(nums), max(nums)
        
        range = (max_val - min_val) // len(nums) + 1
        cnt = (max_val - min_val) // range + 1

        min_vals = [float('inf') for _ in range(cnt)]
        max_vals = [float('-inf') for _ in range(cnt)]

        for num in nums: 
            idx = (num - min_val) // bucket_size
            min_vals[idx] = min(num, min_vals[idx])
            max_vals[idx] = max(num, max_vals[idx])
        maxGap = 0
        for i in range(1, cnt) :
            maxGap = max(maxGap, min_vals[i] - max_vals[i - 1])
        return maxGap

    def maximumGap(self, nums: List[int]) -> int:
        return self.bucket_sort(nums)
        
# @lc code=end

