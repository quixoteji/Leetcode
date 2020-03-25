#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = list(zip(nums, range(len(nums))))
        nums.sort()
        for i in range(len(nums)) :
            j = i + 1
            while j < len(nums) and nums[j][0] - nums[i][0] <= t :
                if abs(nums[j][1] - nums[i][1]) <= k: return True
                else : j += 1
        return False
        

#[1,2,3,1]\n3\n0
        
# @lc code=end

