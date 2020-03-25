#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#

# @lc code=start
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # l1 = [i for i in range(len(words)) if words[i] == word1]
        # l2 = [i for i in range(len(words)) if words[i] == word2]
        # ans = float('inf')
        # for i in l1 :
        #     for j in l2 :
        #         ans = min(ans, abs(i - j))
        idx1, idx2 = float('-inf'), float('-inf')
        shortest = len(words)
        for i, word in enumerate(words): 
            if word == word1 : 
                idx1 = i
                shortest = min(shortest, idx1 - idx2)
            if word == word2 :
                idx2 = i
                shortest = min(shortest, idx2 - idx1)
        return shortest


        
# @lc code=end

