class Solution:
    def generateParenthesis(self, n) :
        ans = []
        curr = ''
        l = r = 0
        self.dfs(ans, curr, l, r, n)
        return ans
    
    def dfs(self, ans, curr, l, r, n) :
        if l + r == 2 * n and l == r :
            ans.append(curr)
            return
        if l < r or l > n or r > n :
            return
        for char in ['(', ')'] :
            if char == '(' :
                self.dfs(ans, curr + char, l + 1, r, n)
            else :
                self.dfs(ans, curr + char, l, r + 1, n)


s = Solution()
s.generateParenthesis(3)
