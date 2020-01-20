#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return self.sol1(s)

    def sol1(self, s) :
        if not s : return [""]
        l, r = 0, 0
        for char in s :
            l += (char == '(')
            if l == 0 : r += (char == ')')
            else : l -= (char == ')')
        ans = []
        self.dfs(s, 0, l, r, ans)
        return ans 

    def isValid(self, s) :
        count = 0
        for char in s :
            if char == '(' : count += 1
            if char == ')' : count -= 1
            if count < 0 : return False
        return count == 0

    def dfs(self, s, start, l, r, ans) :
        if l == 0 and r == 0 :
            if self.isValid(s) : ans.append(s)
            return
        for i in range(start, len(s)) :
            if i != start and s[i] == s[i - 1] : continue
            if s[i] == '(' or s[i] == ')' :
                curr = s[:i] + s[i+1:]
                if r > 0 : self.dfs(curr, i, l, r-1, ans)
                elif l > 0 : self.dfs(curr, i, l-1, r, ans)
                else : pass
    

        
# @lc code=end

