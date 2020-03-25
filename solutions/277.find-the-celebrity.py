#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        return self.sol1(n)

    def sol1(self, n) : 
        candidate = 0
        for i in range(1, n):
            if knows(i, candidate) and not knows(candidate, i):
                continue
            else:
                candidate = i
        for j in range(candidate):
            if not knows(j, candidate) or knows(candidate, j):
                return -1
        return candidate

# @lc code=end

