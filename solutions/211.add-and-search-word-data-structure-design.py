#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start
class TrieNode :
    def __init__(self) :
        self.children = collections.defaultdict(TrieNode)
        self.isword = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word :
            curr = curr.children[char]
        curr.isword = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(curr, i) :
            if i == len(word) : return curr.isword
            if word[i] != '.' :
                curr = curr.children.get(word[i])
                if not curr : return False
                else : return dfs(curr, i + 1)
            else :
                for child in curr.children :
                    if dfs(curr.children[child], i + 1) : return True
                return False

        return dfs(self.root, 0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

