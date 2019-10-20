#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def sol1(self, s) :
        if len(s) <= 1 : return s
        maxlen = 0
        while i < len(s) :
            curr = max(checkodd(i), checkeven(i))
            maxlen = max(curr, maxlen)
        


        



    def longestPalindrome(self, s: str) -> str:
        return self.sol1(s)
        
# @lc code=end

