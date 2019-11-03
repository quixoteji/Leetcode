#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = 0, 0
        for num in nums:
            if cnt == 0 : 
                res = num
                cnt += 1
            else :
                cnt = cnt + 1 if num == res else cnt - 1
        return res

 

        
# @lc code=end

