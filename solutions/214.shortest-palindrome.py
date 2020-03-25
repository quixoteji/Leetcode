#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return self.sol2(s)

    # Solution 1 : * (time limit exceeded)
    def sol1(self, s) :
        if s == s[::-1] : return s
        flag = 1
        while flag :
            s = '*' + s
            if self.isPalindrome(s) : flag = 0
        ans = ''
        for i in range(len(s)) :
            if s[i] == '*' : ans += s[len(s) - i - 1] 
            else : ans += s[i]
        return ans
    
    def isPalindrome(self, s) :
        ps = s[::-1]
        for i in range(len(s)) :
            if ps[i] == '*' or s[i] == '*': continue
            if ps[i] != s[i] : return False
        return True

    # Solution 2 : two strings
    def sol2(self, s) :
        if s == s[::-1] : return s
        ans, ss = '', s[::-1]
        for i in range(len(s)) :
            ts = ss[i:]
            if ts == ts[::-1] : break
        ans = s[len(ts):][::-1] + s
        return ans



        
# @lc code=end

