#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#

# @lc code=start
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        last1, last2 = -1, -1
        same = word1 == word2
        distance = len(words)
        for i , word in enumerate(words):
            if word == word1 :
                if same : last1, last2 = last2, i
                else : last1 = i
            elif word == word2 :
                last2 = i

            if last1 != -1 and last2 != -1 :
                distance = min(distance, abs(last1 - last2))
        return distance
        
# @lc code=end

