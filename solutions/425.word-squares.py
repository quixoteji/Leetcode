#
# @lc app=leetcode id=425 lang=python3
#
# [425] Word Squares
#

# @lc code=start
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)

        ans = []
        word_squares = []
        for word in words :
            word_squares.append(word)
            self.backtracking(1, word_squares, ans)
            word_squares.pop()
        return ans


    def buildTrie(self, words):
        self.trie = {}
        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]

        
# @lc code=end

