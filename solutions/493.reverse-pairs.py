#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.sol1(nums)

    def sol1(self, nums) :
        if not nums : return 0
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2 * nums[j] : ans += 1
        return ans
        
    def sol2(self, nums) :
        stack = []
        for num in nums : 
            if not stack or num < 2 * stack[-1] :
                stack.append(num)
            
# @lc code=end

