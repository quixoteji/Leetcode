#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.sol3(nums)

    def sol1(self, nums) :
        ans = []
        for i in range(len(nums)) :
            product = 1
            for j in range(len(nums)) :
                if i != j : product *= nums[j]
            ans.append(product)
        return ans
        
    def sol2(self, nums):
        left = [1 for num in nums]
        right = [1 for num in nums]
        rt = lt = 1
        for i in range(len(nums)):
            lt *= nums[i]
            rt *= nums[len(nums) - 1 - i]
            left[i] = lt
            right[len(nums) - 1 - i] = rt
        ans = [0 for num in nums]
        print(left)
        print(right)
        for i in range(len(nums)) :
            if i == 0 : ans[i] = right[i + 1]
            elif i == len(nums) - 1 : ans[i] = left[i - 1]
            else : ans[i] = right[i + 1] * left[i - 1]
        return ans


    def sol3(self, nums) :
        ans = [1 for num in nums]
        right = 1
        for i in range(1, len(nums)) : 
            ans[i] = ans[i - 1] * nums[i - 1]
        # print(ans)
        for i in range(len(nums)) :
            j = len(nums) - 1 - i
            ans[j] *= right
            right *= nums[j]
        return ans


# @lc code=end

