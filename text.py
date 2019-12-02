class Solution:
    # Solution 1 : dfs
    def sol1(self, s) :
        if len(s) < 2 : return 0 
        ans = []
        curr = []
        self.dfs(ans, curr, s)
        print(ans)
        return 10

    def dfs(self, ans, curr, s) :
        if not s :
            ans.append(curr[:])
            return 
        for i in range(1, len(s) + 1) :
            ss = s[:i]
            if ss == ss[::-1] :
                curr.append(ss)
                self.dfs(ans, curr, s[i:])
                curr.pop()
    
    def minCut(self, s):
        return self.sol1(s)

A = Solution()
print(A.minCut('abc'))


