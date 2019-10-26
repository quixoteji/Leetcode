class Solution:
    def maxSubArray(self, nums):
        l, r, maxVal = 0, len(nums), float('-inf')
        temp = nums[:]
        while l < r :
            maxVal = max(sum(temp), maxVal)
            if nums[l] < nums[r]:
                l += 1
                temp = nums[l:r]
            else:
                r -= 1
                temp = nums[l:r]
                
        return maxVal
A = Solution()
print(A.maxSubArray([-2,1]))