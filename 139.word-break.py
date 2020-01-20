#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def canBreak(self, s, mem, words):
        if s in mem : return mem[s]
        if s in words:
            mem[s] = True
            return True
        for i in range(1, len(s)) :
            r = s[i : ]
            if r in words and self.canBreak(s[0:i], mem, words):
                mem[s] = True
                return True
        mem[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.canBreak(s, {}, set(wordDict))

# @lc code=end

