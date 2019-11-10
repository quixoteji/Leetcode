#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j, num = 0, 0, ''
        while i < len(word) :
            if word[i] == abbr[j] :
                i, j = i + 1, j + 1
            else :
                if abbr[j].isdigit() :
                    while j < len(abbr) and abbr[j].isdigit() :
                        num += abbr[j]
                        j += 1
                    i += int(num)
                else :
                    return False
        return i == j
        
# @lc code=end

