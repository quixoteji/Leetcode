#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2 : return True
        ans = [1 if _.isupper() else 0 for _ in word]
        if sum(ans) == 0 or sum(ans) == len(word) or (sum(ans) == 1 and ans[0] == 1) :
            return True
        return False
        
# @lc code=end

