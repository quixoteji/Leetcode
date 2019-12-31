#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        return self.sol1(word, abbr)
    
    def sol1(self, word, abbr) :
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j] :
                i, j = i + 1, j + 1
            else :
                if abbr[j].isdigit() :
                    num = ''
                    while j < len(abbr) and abbr[j].isdigit() :
                        num += abbr[j]
                        j += 1
                    # print(int(num))
                    if str(int(num)) != num or int(num) == 0: return False
                    i += int(num)
                else :
                    # print(word[i])
                    # print(abbr[j])
                    return False
        return i == len(word) and j == len(abbr)
        
# @lc code=end

