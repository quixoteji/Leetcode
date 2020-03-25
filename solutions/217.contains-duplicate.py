#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = collections.defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > 1 : return True
            
        return False
# @lc code=end

