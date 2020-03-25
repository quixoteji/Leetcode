import collections
import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node :
    def __init__(self, val) :
        self.val = val
        self.children = {}
        self.suggestions = []

class Trie :
    def __init__(self) :
        self.root = Node(None)

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
                res.append(root.suggestions[:])
                root = root.children[char]
            else :
                break
        remaining = len(word) - len(res)
        for j in range(remaining) :
            res.append([])
        return res

class Solution:
    def solve(self, image, sr, sc, newColor) :
        m, n = len(image), len(image[0])
        queue = []
        queue.append([sr, sc])
        val = image[sr][sc]
        image[sr][sc] = newColor
        d = [1, 0, -1, 0, 1]
        while queue :
            l = len(queue)
            for _ in range(l) :
                r, c = queue.pop(0)
                for i in range(4) :
                    ir, ic = r + d[i], c + d[i + 1]
                    while 0 <= ir < m and 0 <= ic < n :
                        if image[ir][ic] == val :
                            image[ir][ic] = newColor
                            queue.append([ir, ic])
        return image
            

A = Solution()
print(A.solve([[0,0,0],[0,1,1]], 1, 1, 1))


