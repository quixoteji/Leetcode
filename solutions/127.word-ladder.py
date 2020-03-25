#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def bi_bfs(self, beginWord, endWord, wordList) :
        if len(beginWord) != len(endWord) or endWord not in wordList : return 0
        wordList = set(wordList)     
        wordLen = len(beginWord)
        s1, s2 = {beginWord}, {endWord}
        wordList.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0 :
            step += 1
            (s1, s2) = (s2, s1) if len(s1) > len(s2) else (s1, s2)
            s = set()
            for word in s1 :
                nextWords = [word[:i] + t + word[i+1:] for t in 'abcdefghijklmnopqrstuvwxyz' for i in range(wordLen)]
                for nextWord in nextWords :
                    if nextWord in s2 : return step + 1
                    if nextWord not in wordList : continue
                    wordList.remove(nextWord)
                    s.add(nextWord)
            s1 = s
        return 0

    def bfs(self, beginWord, endWord, wordList) :
        if len(beginWord) != len(endWord) or endWord not in wordList : return 0
        wordList = set(wordList)
        queue = []
        queue.append(beginWord)
        wordLen, step = len(beginWord), 0
        while queue :
            step += 1
            queueLen = len(queue)
            for _ in range(queueLen) :
                word = list(queue.pop(0))
                for i in range(wordLen) :
                    ch = word[i]
                    for j in range(26) :
                        nch = chr(ord('a') + j)
                        if ch == nch : continue
                        word[i] = nch
                        next_word = ''.join(word)
                        if next_word == endWord : return step + 1
                        if next_word not in wordList : continue
                        wordList.remove(next_word)
                        queue.append(next_word)
                    word[i] = ch
        return 0


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.bi_bfs(beginWord, endWord, wordList)


        
# @lc code=end

