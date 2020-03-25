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
            for j in range(i, len(s)) :
                if s[j] == '(' : count += 1
                if s[j] == ')' : count -= 1
                if count < 0 : break
                if count == 0 : maxlen = max(j - i + 1, maxlen)
        return maxlen

    def stack_solution(self, s) :
        stack = []
        start, maxlen = 0, 0
        for i in range(len(s)) :
            if s[i] == '(' : 
                stack.append(i)
                continue
            if not stack :
                start = i + 1
            else :
                stack.pop()
                maxlen = max(maxlen, i - stack[-1] if stack else i - start + 1)
        return maxlen

    def dp(self, s) :
        if not s : return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)) :
            if s[i] == ')' :
                if s[i - 1] == '(' :
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else :
                    if i - dp[i - 1] > 0 and s[i - dp[i-1] - 1] == '(' :
                        dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
        
        return max(dp)

    def longestValidParentheses(self, s: str) -> int:
        return self.dp(s)
        
# @lc code=end

