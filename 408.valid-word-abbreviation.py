#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def abbr2word(self, abbr) :
        s = ''
        num = ''
        for i, char in enumerate(abbr) :
            if not char.isdigit() : 
                if num :
                    if num.startswith('0') : 
                        return False 
                    s += int(num) * '.'
                s += char
                num = ''
            else : 
                num += char
        if num : 
            if num.startswith('0') : 
                return False 
            s += int(num) * '.'
        return s

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = ''
        while i < len()

        
# @lc code=end

