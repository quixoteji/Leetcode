#
# @lc app=leetcode id=288 lang=python3
#
# [288] Unique Word Abbreviation
#

# @lc code=start
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = collections.defaultdict(set)
        for word in dictionary:
            if len(word) >=2: self.d[(word[0]+word[-1],len(word))].add(word)

        
    def isUnique(self, word: str) -> bool:
        return False if len(word) > 2 and (len(self.d[(word[0]+word[-1],len(word))]) > 1 or(len(self.d[(word[0]+word[-1],len(word))]) == 1 and word not in self.d[(word[0]+word[-1],len(word))])) else True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# @lc code=end

