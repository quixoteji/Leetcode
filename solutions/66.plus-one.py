#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)):
            n = len(digits) - 1 - i
            if n == len(digits) - 1: carry, digits[n] = divmod(carry + digits[n] + 1, 10)
            else : carry, digits[n] = divmod(carry + digits[n], 10)
        if carry : digits.insert(0, 1)
        return digits
            
        
# @lc code=end

