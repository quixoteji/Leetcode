#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self) :
        self.children = collections.defaultdict(TrieNode)
        self.isword = False

class Trie:
    def __init__(self) :
        self.root = TrieNode()
    def add(self, word):
        curr = self.root
        for char in word :
            curr = curr.children[char]
        curr.isword = word

class Solution:
    def __init__(self) :
        self.trie= None
        self.board = None
        self.ans = set()
    def dfs(self, i, j, curr) :
        if self.board[i][j] not in curr.children : return
        else :
            curr = curr.children[self.board[i][j]]
            if not curr : return
            else :
                if bool(curr.isword) : self.ans.add(curr.isword)
                temp = self.board[i][j]
                self.board[i][j] = '#'
                if i-1 >= 0 : self.dfs(i-1, j, curr)
                if i+1 < len(self.board) : self.dfs(i+1, j, curr)
                if j-1 >= 0 : self.dfs(i, j-1, curr)
                if j+1 < len(self.board[0]) : self.dfs(i, j+1, curr)
                self.board[i][j] = temp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.trie = Trie()
        for word in words : self.trie.add(word)
        r, c = len(self.board), len(self.board[0])
        for i in range(r) :
            for j in range(c) :
                curr = self.trie.root
                self.dfs(i, j, curr)
        return list(self.ans)
        
# @lc code=end

