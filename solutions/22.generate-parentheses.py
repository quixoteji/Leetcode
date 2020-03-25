#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def helper(self, ans, s, l, r, n) :
        if r > l or r > n or l > n: return
        if l == r and l == n and len(s) == 2 * n: 
            ans.append(s)
        
        for char in ['(', ')'] :
            if char == '(' : l += 1
            if char == ')' : r += 1
            s += char
            self.helper(ans, s, l, r, n)
            s = s[:-1]
            if char == '(' : l -= 1
            if char == ')' : r -= 1
             
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = ''
        l, r = 0, 0
        self.helper(ans, s, l, r, n) 
        return ans
        
# @lc code=end

