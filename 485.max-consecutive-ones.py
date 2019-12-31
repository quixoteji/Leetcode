#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        record = ans = 0
        for num in nums :
            if num == 1 : record += 1
            else : 
                ans = max(ans, record)
                record = 0
        return max(ans, record)
        
# @lc code=end

