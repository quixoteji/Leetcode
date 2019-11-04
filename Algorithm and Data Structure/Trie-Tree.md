# Trie (Prefix Tree)

## What is Trie?
A Trie is a special form of a Nary tree, used to store strings.

## Basic Operation
1. Insert : O(m)
2. Search (word or prefix): O(m)

m is the length of the string.

*Note:*
1. No collision for Different keys in Trie
2. Key is in dictionary representation

## Comparison with Hashtable
1. Time Complexity

    The time complexity to search in hash table is typically O(1), but will be O(logN) in the worst time if there are too many collisions and we solve collisions using height-balanced BST.

    The time complexity to search in Trie is O(M).

    The hash table wins in most cases.

2. Space Complexity

    The space complexity of hash table is O(M * N). If you want hash table to have the same function with Trie, you might need to store several copies of the key. For instance, you might want to store "a", "ap", "app", "appl" and also "apple" for a keyword "apple" in order to search by prefix. The space complexity can be even much larger in that case.

    The space complexity of Trie is O(M * N) as we estimated above. But actually far smaller than the estimation since there will be a lot of words have the similar prefix in real cases.

    Trie wins in most cases.

## Application
1. Count the number of words
2. Match strings
3. Match prefixes
4. Order strings

## Python for Trie
```python
class TrieNode :
    def __init__(self) :
        self.children = collections.defaultdict(TrieNode)
        self.isword = False

class Trie :
    def __init__(self) :
        self.root = TrieNode()
    def insert(self, word) :
        currnt = self.root
        for char in word :
            currnt = currnt.children[char]
        currnt.isword = True
    def self(self, word) :
        currnt = self.root
        for char in word :
            currnt = currnt.children.get(char)
            if not currnt: return False
        return currnt.isword
    def startsWith(self, prefix) :
        currnt = self.root :
        for char in prefix :
            currnt = currnt.children.get(char)
            if not currnt: return False
        return True
```
