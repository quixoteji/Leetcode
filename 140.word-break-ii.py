#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.sol1(s, wordDict)

    def sol1(self, s, wordDict) :
        words = set(wordDict)
        mem = dict()
        return self.canBreak(s, mem, words)

    def canBreak(self, s, mem, words) :
        if s in mem : return mem[s]
        ans = []
        if s in words : ans.append(s)
        for i in range(1, len(s)) :
            r = s[i:]
            if r not in words : continue
            ans += [w + " " + r for w in self.canBreak(s[0:i], mem, words)]
        mem[s] = ans
        return mem[s]


        
# @lc code=end

