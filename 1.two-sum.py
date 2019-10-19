#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums) :
            if num in hashmap : return [hashmap[num], i]
            else : hashmap[target - num] = i
# @lc code=end

