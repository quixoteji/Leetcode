#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while True:
            if n == 1 : return True
            if n in hashset: return False
            hashset.add(n)
            k = 0
            while n > 0 :
                n, r = divmod(n, 10)
                k += r ** 2
            n = k
# @lc code=end

