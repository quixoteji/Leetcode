#
# @lc app=leetcode id=293 lang=python3
#
# [293] Flip Game
#

# @lc code=start
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        if not s : return []
        ans, s = [], list(s)
        for i in range(len(s)) :
            if s[i] == '+' and i + 1 < len(s) :
                if s[i + 1] == '+' : 
                    s[i : i + 2] = '-','-'
                    ans.append(''.join(s))
                    s[i : i + 2] = '+','+'
        return ans
# @lc code=end

