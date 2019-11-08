#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        num = 0
        for key in counter :
            num += counter[key] // 2 * 2
        return num if num == len(s) else num + 1
        
# @lc code=end

