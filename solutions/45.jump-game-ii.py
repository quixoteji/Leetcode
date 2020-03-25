#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = last_cover = curr_cover = 0
        for i in range(len(nums)) :
            if last_cover < i :
                last_cover = curr_cover
                steps += 1
            if last_cover >= len(nums) - 1 :
                return steps
            curr_cover = max(curr_cover, nums[i] + i);
        return steps


        
# @lc code=end

