#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.sol2(nums)

    def sol1(self, nums) :
        if not nums : return False
        for i in range(len(nums)) :
            for j in range(i + 1, len(nums)):
                    for k in range(j + 1, len(nums)) :
                        if nums[i] < nums[k] < nums[j]:
                            return True
        return False

    def sol2(self, nums) :
        deq = collections.deque()
        num2 = None
        
        for n in nums[::-1]:
            if num2 is not None and n < num2:
                return True
            while deq and deq[-1] < n:
                num2 = deq.pop()
            deq.append(n)
        return False
                
        
# @lc code=end

