#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums) :
            if num in hashmap.keys():
                return [hashmap[num], i]
            else :
                hashmap[target - num] = i

