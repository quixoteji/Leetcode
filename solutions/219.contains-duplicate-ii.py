#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for i, num in enumerate(nums):
            if num in hashmap and i - hashmap[num] <= k : return True
            else : hashmap[num] = i
        return False

        
# @lc code=end

