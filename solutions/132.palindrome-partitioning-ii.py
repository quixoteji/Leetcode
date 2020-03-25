#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    # Solution 1 : dfs
    # Time Limit Exceeded
    def sol1(self, s) :
        if len(s) < 2 : return 0 
        ans = []
        curr = []
        self.dfs(ans, curr, s)
        return min(ans)

    def dfs(self, ans, curr, s) :
        if not s :
            ans.append(len(curr) - 1)
            return 
        for i in range(1, len(s) + 1) :
            ss = s[:i]
            if ss == ss[::-1] :
                curr.append(ss)
                self.dfs(ans, curr, s[i:])
                curr.pop()

    # Solution 2 : DP
    def sol2(self, s) :
        if len(s) < 2 : return 0
        n = len(s)
        p = [[False for _ in range(n)] for _ in range(n)]
        dp = [0 for _ in range(n)]
        for i in range(n) :
            dp[i] = i
            for j in range(i + 1) :
                if s[i] == s[j] and (i - j < 2 or p[j + 1][i - 1]) :
                    p[j][i] = True
                    dp[i] = 0 if j == 0 else min(dp[i], dp[j - 1] + 1)
        return dp[n - 1]

    # Solution 3 : DP
    def sol3(self, s) :
        dp = [x for x in range(-1, len(s))]
        for i in range(len(s)) :
            for j in range(i, len(s)) :
                if s[i : j] == s[i : j : -1] :
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        return dp[-1]

    # Solution 4 : DP + memorization
        # algorithm
    # cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
    # for i in range(len(s)):
    #     r1, r2 = 0, 0
    #     # use i as origin, and gradually enlarge radius if a palindrome exists
    #     # odd palindrome
    #     while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
    #         cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
    #         r1 += 1
    #     # even palindrome
    #     while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
    #         cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
    #         r2 += 1
    # return cut[-1]

    def minCut(self, s: str) -> int:
        return self.sol2(s)
        
# @lc code=end

