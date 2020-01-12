#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.sol1(nums)

    def sol1(self, nums) :
        nums.sort()
        ans = []
        queue = []

        for i in range(len(nums) + 1) :
            if i == 0 :
                queue.append([])
                ans.append([])
            else :
                 

        
        
# @lc code=end

