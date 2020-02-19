#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#

# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered = 0
        ans = 0
        idx = 0
        while covered < n and idx < len(nums) :
            num = nums[idx]
            while covered < n and covered < num - 1 :
                ans += 1
                covered += covered + 1
            covered += num
            idx += 1
        
        while covered < n :
            ans += 1
            covered += covered + 1

        return ans

        
# @lc code=end

