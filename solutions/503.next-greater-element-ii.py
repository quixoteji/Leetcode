#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return self.sol2(nums)

    # Brutal_Force
    def sol1(self, nums) :
        ans = [-1 for _ in nums]
        for i in range(len(nums)) :
            for j in range(len(nums)) :
                k = (i + j) % len(nums) 
                if nums[k] > nums[i] : 
                    ans[i] = nums[k]
                    break
        return ans

    # stack
    def sol2(self, nums) :
        stack = []
        ans = [-1 for _ in nums]
        for i in range(2 * len(nums)) :
            num = nums[i % len(nums)]
            while stack and nums[stack[-1]] < num :
                ans[stack.pop()] = num
            if i < len(nums) : stack.append(i)
        return ans


        
# @lc code=end

