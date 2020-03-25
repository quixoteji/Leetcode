#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#

# @lc code=start
class WordDistance:

    def __init__(self, words: List[str]):
        self.words_indices = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.words_indices[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.words_indices[word1], self.words_indices[word2]
        distance = float('inf')
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2) :
            distance = min(distance, abs(l1[p1] - l2[p2]))
            if l1[p1] < l2[p2] : p1 += 1
            else : p2 += 1
        return distance
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
# @lc code=end

