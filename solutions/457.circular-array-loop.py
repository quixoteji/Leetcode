#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        return self.sol1(nums)

    def sol1(self, nums) :
        N = len(nums)
        visited = 10000
        self.mark = 10000

        for i in range(N) :
            if (i + nums[i] + N) % N == i :
                nums[i] = visited
        
        def move(i, direction) :
            this = nums[i]
            if this == self.mark :
                return True
            if this

        
# @lc code=end

