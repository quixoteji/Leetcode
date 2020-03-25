#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        last_seen = lower - 1
        nums.append(upper + 1)
        for num in nums :
            if num == last_seen + 2 : 
                ans.append(str(last_seen + 1))
            elif num > last_seen + 2 : 
                ans.append(str(last_seen + 1) + '->' + str(num - 1))
            last_seen = num
            
        return ans



        
# @lc code=end

