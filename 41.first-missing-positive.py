#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) < 1 : return 1
        flag, n, ans = 0, len(nums), 1
        for num in nums :
            if num == 1 : flag = 1
            if num < 1 or num > n :
                num = 1    
            num = 1 << num
            ans = ans | num 
        
        if not flag : return 1
        for i in range(n + 1) :
            temp = 1 << i
            if temp & ans == 0 : 
                return i
        return n + 1

        
# @lc code=end

