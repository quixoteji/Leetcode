#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.sol2(nums)

    def sol1(self, nums) :
        return self.getScore(nums, 0, len(nums) - 1) >= 0

    def getScore(self, nums, l, r) :
        if l == r : return nums[l]
        return max(nums[l] - self.getScore(nums, l + 1, r), \
            nums[r] - self.getScore(nums, l, r - 1))

    def sol2(self, nums) :
        self.mem = [0] * (len(nums) * len(nums))
        return self.getScore2(nums, 0, len(nums) - 1) >= 0

    def getScore2(self, nums, l, r) :
        if l == r : return nums[l]
        k = l * len(nums) + r
        if self.mem[k] : return self.mem[k]
        self.mem[k] = max(nums[l] - self.getScore2(nums, l + 1, r), \
            nums[r] - self.getScore2(nums, l, r - 1))
        return self.mem[k]
        
# @lc code=end

