#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    d2c = {'2' : 'abc', '3' : 'def', 
            '4' : 'ghi', '5' : 'jkl', '6' : 'mno',
            '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'} 

    def helper(self, ans, s, digits, i) :
        if len(s) == len(digits) : 
            ans.append(s)
            return
        for char in self.d2c[digits[i]] :
            s += char
            self.helper(ans, s, digits, i + 1)
            s = s[:-1]
        

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 : return []
        ans = []
        s = ''
        self.helper(ans, s, digits, 0)
        return ans

        
# @lc code=end

