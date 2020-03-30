# Trie

**Trie**, also called **prefix tree** or **digital tree**, is a kind of search tree (an ordered tree data structure used to store a dynamic set or associative array)

![Trie](./pic/trie.png)

## Python Implementation

```python
class Node :

    def __init__(self) :
        self.children = collections.defaultdict(Node)
        self.isLeaf = False

class Trie :

    def __init__(self) :
        self.root = Node()

    def insert(self, word) :
        curr = self.root
        for char in word :
            curr = curr.children[char]
        curr.isLeaf = True

    def search(self, word) :
        curr = self.root
        for char in word :
            curr = curr.children.get(char)
            if not curr : return False
        return True

```