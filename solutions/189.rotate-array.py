#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums : nums
        for i in range(k) :
            temp = nums.pop()
            nums.insert(0, temp)
        return nums
        
# @lc code=end

