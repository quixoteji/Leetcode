#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    # Solution 1 : O(n^2)
    def sol1(self, s, nums) :
        if not nums or sum(nums) < s: return 0
        minLen, n = len(nums), len(nums)
        for i in range(n) :
            r = n
            while r >= i : 
                if sum(nums[i:r]) >= s : 
                    minLen = min(minLen, len(nums[i:r]))
                    r -= 1
                else : break
        return minLen
    # Solution 2 : two pointers
    def sol2(self, s, nums) :
        if not nums : return 0
        minLen, start, curr = len(nums) + 1, 0, 0
        for i, num in enumerate(nums) : 
            curr += num
            while curr >= s :
                minLen = min(minLen, i - start + 1)
                curr -= nums[start]
                start += 1
        return minLen if minLen <= len(nums) else 0


    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        return self.sol2(s, nums)

        
# @lc code=end

