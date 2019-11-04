#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Node :
    def __init__(self) :
        self.children = collections.defaultdict(Node)
        self.isword = -1

class Trie :
    def __init__(self) :
        self.root = Node()
    def add(self, word, val) :
        curr = self.root
        for char in word :
            curr = curr.children[char]
        curr.isword = val
    def search(self, word) :
        curr = self.root
        for char in word :
            curr = curr.children.get(char)
            if not curr : return -1
        return curr.isword

class Solution:
    def brute_force(self, words) :
        ans = []
        for i in range(len(words)) :
            for j in range(len(words)) :
                if i != j :
                    s = words[i] + words[j]
                    if s == s[::-1] :
                        ans.append([i,j])
        return ans

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        T = Trie()
        for i, word in enumerate(words):
            T.add(word[::-1], i)
        ans = []
        for i, word in enumerate(words):
            for idx in range(len(word)) :
                rw, lw = word[:idx], word[idx:]
                if rw == rw[::-1] and T.search(lw) != -1 and idx != T.search(lw): 
                    ans.append([idx, T.search(lw)])
                if lw == lw[::-1] and T.search(rw) != -1 and idx != T.search(rw): 
                    ans.append([idx, T.search(rw)])
        return ans

        
        
# @lc code=end

