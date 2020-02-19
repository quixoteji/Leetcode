#
# @lc app=leetcode id=734 lang=python3
#
# [734] Sentence Similarity
#

# @lc code=start
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        return self.sol1(words1, words2, pairs)

    def sol1(self, words1, words2, pairs) : 
        if len(words1) != len(words2): return False
        if not pairs : return words1 == words2
        hashmap = collections.defaultdict(set)
        for pair in pairs :
            hashmap[pair[0]].add(pair[1])
            hashmap[pair[1]].add(pair[0])

        for i in range(len(words1)):
            if words1[i] != words2[i] and words2[i] not in hashmap[words1[i]]:
                return False
        
        return True
                

        

        
# @lc code=end

