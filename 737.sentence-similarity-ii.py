#
# @lc app=leetcode id=737 lang=python3
#
# [737] Sentence Similarity II
#

# @lc code=start
class Solution:
    class Union_find_set():
        def __init__(self, n) :
            self._parents = [i for i in range(n)]
            self._ranks = [1 for i in range(n)]
        def find(self, x) :
            if x != self._parents[x] :
                self._parents[x] = self.find(self._parents[x])
            return self._parents[x]
        def union(self, x, y) :
            px, py = self.find(x), self.find(y)
            if px == py : return False
            if self._ranks[px] < self._ranks[py] : 
                self._parents[px] = py
            elif self._ranks[px] > self._ranks[py] :
                self._parents[py] = px
            else : 
                self._parents[py] = px
                self._ranks[px] += 1
            return True

    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        hset = set()
        for word in words1 + words2:
            hset.add(word)
        for pair in pairs :
            hset.add(pair[0])
            hset.add(pair[1])
        ufSet = self.Union_find_set(2 * len(list(hset)))
        hmap = {}
        for i, v in enumerate(list(hset)):
            hmap[v] = i
        
        for pair in pairs :
            u = hmap[pair[0]]
            v = hmap[pair[1]]
            ufSet.union(u, v)

        for i in range(len(words1)):
            u = ufSet.find(hmap[words1[i]])
            v = ufSet.find(hmap[words2[i]])
            if u != v : return False
        return True
        
# @lc code=end

