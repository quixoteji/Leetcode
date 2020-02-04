#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        return self.sol1(nums)

    def sol1(self, nums) :
        if not nums : return []
        ans = []
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1 : end = nums[i]
            else :
                if start == end : ans.append(str(start))
                else : ans.append(str(start) + '->' + str(end))
                start = end = nums[i]
        if start == end : ans.append(str(start))
        else : ans.append(str(start) + '->' + str(end))
        return ans
                

        
# @lc code=end

