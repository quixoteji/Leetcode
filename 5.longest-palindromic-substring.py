#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def sol1(self, s) :
        if len(s) <= 1 : return s
        l, ans = len(s), ''
        for i in range(len(s)) :
            for j in range(len(s)) :
                if i - j < 0 or i + j >= l or s[i - j] != s[i + j] :
                    break
                ans = ans if len(ans) > len(s[i - j : i + j + 1]) else s[i - j : i + j + 1]
            if i + 1 < l and s[i] == s[i + 1] : 
                for j in range(len(s)) :
                    if i - j < 0 or i + j + 1 >= l or s[i - j] != s[i + j + 1] :
                        break
                    ans = ans if len(ans) > len(s[i - j : i + j + 2]) else s[i - j : i + j + 2]
        return ans

    def sol2(self, s) :
        pass
        
    def longestPalindrome(self, s: str) -> str:
        return self.sol1(s)
        
# @lc code=end

