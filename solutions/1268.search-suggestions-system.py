#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Node :
    def __init__(self, val) :
        self.val = val
        self.children = {}
        self.suggestions = []

class Trie :
    def __init__(self) :
        self.root = Node('A')

    def insert(self, word) :
        root = self.root 
        for char in word :
            if char not in root.children :
                root.children[char] = Node(char)
            if len(root.suggestions) < 3 :
                root.suggestions.append(word)
            root = root.children[char]
        if len(root.suggestions) < 3 :
            root.suggestions.append(word)

    def find(self, word):
        root = self.root
        res = []
        for char in word :
            if char in root.children :
                root = root.children[char]
                res.append(root.suggestions)    
            else :
                break
        remaining = len(word) - len(res)
        for j in range(remaining) :
            res.append([])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if len(products) == 1 and products[0] == searchWord :
            return [[searchWord] for i in range(len(searchWord))]
        products.sort()
        trie = Trie()
        for product in products :
            trie.insert(product)
        return trie.find(searchWord)
        
# @lc code=end

