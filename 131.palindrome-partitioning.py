#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.sol2(s)

    # Solution 1 : DFS
    def sol1(self, s) :
        if len(s) < 1 : return [[s]]
        ans = []
        curr = []
        self.dfs(ans, curr, s)
        return ans

    def dfs(self, ans, curr, s) :
        if not s :
            ans.append(curr[:])
            return 
        for i in range(1, len(s) + 1) :
            ss = s[: i]
            if self.isPalindrome(ss) :
                curr.append(ss)
                self.dfs(ans, curr, s[i:])
                curr.pop()

    def isPalindrome(self, s) :
        return s == s[::-1] if s else False
        
    # Solution 2 : DP
    # dp[i][j] : check s[i:j] isPalidrome
    def sol2(self, s) :
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n) :
            for j in range(i + 1) :
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1]) :
                    dp[j][i] = True
        ans = []
        curr = []
        self.helper(s, 0, dp, curr, ans)
        return ans

    def helper(self, s, start, dp, curr, ans) :
        if start == len(s) :
            ans.append(curr[:])
            return
        for i in range(start, len(s)) :
            if not dp[start][i] : continue
            curr.append(s[start : i + 1])
            self.helper(s, i + 1, dp, curr, ans)
            curr.pop()

    # Solution 3 : DP
    def sol3(self, s) :
        n = len(s)
        dp = [[False] * 3] * 3
        ans = [[list() for _ in range(n)] for _ in range(n)]
        for i in range(n) :
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j - 1][i + 1]) : 
                    dp[j][i] = True
                    ss = s[j:i+1]
                    for l in ans[j] :
                        l.append(ss)
                        ans[i].append(l)
        return ans

# @lc code=end

