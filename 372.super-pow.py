#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return a ** int(''.join(str(c) for c in b)) % 1337
        
# @lc code=end

