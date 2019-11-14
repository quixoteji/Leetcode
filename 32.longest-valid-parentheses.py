#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def brutal_force(self, s) :
        maxlen = 0
        for i in range(len(s)) :
            count = 0 
            for char in s[i:] :
                if char == '(' : count += 1
                elif char == ')' : count -= 1

                if count < 0 : break
                if count == 0 : maxlen = max(maxlen, count)
        return maxlen
        
    def longestValidParentheses(self, s: str) -> int:
        return self.brutal_force(s)
        
# @lc code=end

