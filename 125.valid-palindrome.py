#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for char in s :
            if char.isalpha() or char.isdigit(): t += char.lower()
        if not t : return True
        return t == t[::-1]
        
# @lc code=end

