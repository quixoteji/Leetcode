#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        maxLen = 0
        firstZero = True
        cutOff = 0
        for i in range(len(nums)) :
            if nums[i] == 1 : curr += 1
            else :
                if firstZero :
                    cutOff = i
                    firstZero = False
                    curr += 1
                else :
                    curr = i - cutOff
                    cutOff = i
            maxLen = max(maxLen, curr)
        return maxLen

        
# @lc code=end

