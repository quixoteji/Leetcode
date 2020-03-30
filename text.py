import collections
# import math

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Node :
#     def __init__(self, val) :
#         self.val = val
#         self.children = {}
#         self.suggestions = []

# class Trie :
#     def __init__(self) :
#         self.root = Node(None)

#     def insert(self, word) :
#         root = self.root 
#         for char in word :
#             if char not in root.children :
#                 root.children[char] = Node(char)
#             if len(root.suggestions) < 3 :
#                 root.suggestions.append(word)
#             root = root.children[char]
#         if len(root.suggestions) < 3 :
#             root.suggestions.append(word)

#     def find(self, word):
#         root = self.root
#         res = []
#         for char in word :
#             if char in root.children :
#                 res.append(root.suggestions[:])
#                 root = root.children[char]
#             else :
#                 break
#         remaining = len(word) - len(res)
#         for j in range(remaining) :
#             res.append([])
#         return res

# class Solution:
#     def solve(self, image, sr, sc, newColor) :
#         m, n = len(image), len(image[0])
#         queue = []
#         queue.append([sr, sc])
#         val = image[sr][sc]
#         image[sr][sc] = newColor
#         d = [1, 0, -1, 0, 1]
#         while queue :
#             l = len(queue)
#             for _ in range(l) :
#                 r, c = queue.pop(0)
#                 for i in range(4) :
#                     ir, ic = r + d[i], c + d[i + 1]
#                     while 0 <= ir < m and 0 <= ic < n :
#                         if image[ir][ic] == val :
#                             image[ir][ic] = newColor
#                             queue.append([ir, ic])
#         return image
            

class Node :
    def __init__(self) :
        self.children = collections.defaultdict(Node)
        self.isLeaf = False
        self.word = None
        
class Trie :
    def __init__(self) :
        self.root = Node()
        
    def insert(self, word) :
        curr = self.root
        for char in word :
            curr = curr.children[char]
        curr.isLeaf = True
        curr.word = word

class Solution:
    def findWords(self, board, words) :
        trie = Trie()
        for word in words :
            trie.insert(word)
        ans = []
        m, n = len(board), len(board[0])
        
        for i in range(m) :
            for j in range(n) :
                visited = set()
                curr = trie.root
                if board[i][j] in curr.children :
                    self.search(curr, i, j, board, visited, ans)
        return ans
    
    def search(self, curr, i, j, board, visited, ans) :
        curr = curr.children.get(board[i][j])
        if not curr : return 
        elif curr.isLeaf :
            ans.append(curr.word)
            return
        
        d = [1, 0, -1, 0, 1]
        m, n = len(board), len(board[0])
        for _ in range(4) :
            di, dj = i + d[_], j + d[_ + 1]
            if 0 <= di < m and 0 <= dj < n and (di, dj) not in visited :
                visited.add((di, dj))
                self.search(curr, di, dj, board, visited, ans)
                visited.remove((di, dj))

a = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

b = [["a","a"]]

c = ["aaa"]
# print(a.findWords(board, words))
print(a.findWords(b, c))