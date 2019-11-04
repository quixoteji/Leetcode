import collections
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
    def dfs(self, i, j, curr, seen) :
        idx = i * len(self.board[0]) + j
        if self.board[i][j] not in curr.children or idx in seen : return
        else :
            curr = curr.children[self.board[i][j]]
            if not curr : return
            elif bool(curr.isword) :
                self.ans.add(curr.isword)
                return
            else :
                seen.add(idx)
                if i-1 >= 0 : self.dfs(i-1, j, curr, seen)
                if i+1 < len(self.board) : self.dfs(i+1, j, curr, seen)
                if j-1 >= 0 : self.dfs(i, j-1, curr, seen)
                if j+1 < len(self.board[0]) : self.dfs(i, j+1, curr, seen)
                return

    def findWords(self, board, words):
        self.board = board
        self.trie = Trie()
        for word in words : self.trie.add(word)
        r, c = len(self.board), len(self.board[0])
        for i in range(r) :
            for j in range(c) :
                curr = self.trie.root
                seen = set()
                self.dfs(i, j, curr, seen)
        return list(self.ans)



A= Solution()
print(A.findWords([["a","b"],["c","d"]],["acdb"]))


[["b","a","a","b","a","b"],
["a","b","a","a","a","a"],
["a","b","a","a","a","b"],
["a","b","a","b","b","a"],
["a","a","b","b","a","b"],
["a","a","b","b","b","a"],
["a","a","b","a","a","b"]]
' +
  '["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]