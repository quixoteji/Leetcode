import collections

class Solution:
    def abbr2word(self, abbr) :
        s = ''
        num = ''
        for i, char in enumerate(abbr) :
            if not char.isdigit() : 
                if num : s += int(num) * '.'
                s += char
                num = ''
            else : 
                num += char
        if num : s += int(num) * '.'
        return s

    def validWordAbbreviation(self, word, abbr):
        _word = self.abbr2word(abbr)
        print(_word)
        print(word)
        # for i in range(len(word)) :
        #     if word[i] == _word[i] or _word[i] == '.' : continue
        #     else : return False
        return True

A = Solution()
b = A.validWordAbbreviation('internationalization',"i12iz4n")
