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
        p1, p2 = 0, len(nums)
        while p1 <= p2 :
            if sum(nums[p1 : p2]) >= s : 
                if nums[p1] > nums[p2 - 1] : p1 += 1
                else : p2 -= 1
            else :
                break
        print(p1, p2)
        return p2 - p1
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        return self.sol2(s, nums)

        
# @lc code=end

