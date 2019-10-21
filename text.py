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
             
        
    def generateParenthesis(self, n):
        ans = []
        s = ''
        l, r = 0, 0
        self.helper(ans, s, l, r, n) 
        return ans

A = Solution()
print(A.generateParenthesis(3))