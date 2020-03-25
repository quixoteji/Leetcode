#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        ans = 0
        for i, u in enumerate(binary[::-1]):
            if u == '0':
                ans += 2 ** i
        return ans
        
# @lc code=end

