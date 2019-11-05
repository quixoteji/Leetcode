#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap : 
                if i - hashmap[num] > k + 1: return False
            hashmap[num] = i
        return True

        
# @lc code=end

