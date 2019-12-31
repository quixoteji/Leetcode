#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation
#

# @lc code=start
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self._dict = set()
        for word in dictionary : self._dict.add(self.abbr(word))
            

    def abbr(self, word) :
        if len(word) < 3 : return word
        else : return word[0] + str(len(word)-2) + word[-1]


    def isUnique(self, word: str) -> bool:
        return self.abbr(word) not in self._dict
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# @lc code=end

