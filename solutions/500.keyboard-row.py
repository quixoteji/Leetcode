#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def word2val(self, word) :
        keyboard = {'qwertyuiop' : 1, 'asdfghjkl' : 2, 'zxcvbnm' : 4}
        ans = 7
        for char in word.lower() :
            if char in 'qwertyuiop' : ans &= keyboard['qwertyuiop']
            if char in 'asdfghjkl' : ans &= keyboard['asdfghjkl']
            if char in 'zxcvbnm' : ans &= keyboard['zxcvbnm']
        return ans
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words :
            if self.word2val(word) == 0 : continue
            ans.append(word)
        return ans
        
# @lc code=end

