#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.sol2(word1, word2)

    # memorization recurrsion
    d = None
    def sol1(self, word1, word2) :
        l1, l2 = len(word1), len(word2)
        self.d = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        return self.minDis(word1, word2, l1, l2)

    def minDis(self, word1, word2, l1, l2) :
        if l1 == 0 : return l2
        if l2 == 0 : return l1
        if self.d[l1][l2] >= 0 : return self.d[l1][l2]
        if word1[l1-1] == word2[l2-1] :
            ans = self.minDis(word1, word2, l1 - 1, l2 - 1)
        else :
            a = self.minDis(word1, word2, l1 - 1, l2 - 1)
            b = self.minDis(word1, word2, l1 - 1, l2)
            c = self.minDis(word1, word2, l1, l2 - 1)
            ans = min(a, b, c) + 1
        self.d[l1][l2] = ans
        return ans

    # dp
    def sol2(self, word1, word2) :
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1 + 1) : dp[i][0] = i
        for j in range(l2 + 1) : dp[0][j] = j
        for i in range(1, l1 + 1) :
            for j in range(1, l2 + 1) :
                c = 0 if word1[i - 1] == word2[j - 1] else 1
                dp[i][j] = min(dp[i-1][j-1]+c, min(dp[i-1][j], dp[i][j-1])+1)
        return dp[l1][l2]

    

        
# @lc code=end

