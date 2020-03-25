#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 : return 0
        if N == 1 : return 1
        p1, p2 = 0, 1
        for i in range(2, N + 1) :
            curr = p1 + p2
            p1, p2 = p2, curr
        return curr
        
# @lc code=end

