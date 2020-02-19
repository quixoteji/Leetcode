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

class Solution:
    def str2tree(self, s) :
        return self.sol1(s)

    def sol1(self, s):
        if not s : return None
        if '(' not in s :
            root = None if s == '-' else TreeNode(int(s))
        else :
            idx = s.find('(')
            root = self.sol1(s[: idx])
            l, r, i = 1, 0, idx + 1
            while i < len(s) :
                if s[i] == '(' : l += 1
                elif s[i] == ')' : r += 1
                if l == r : break
                i += 1
            root.left = self.sol1(s[idx + 1 : i]) 
            root.right = self.sol1(s[i + 1 :]) 
        return root


A = Solution()
z = A.str2tree("4(2(3)(1))(6(5))")
print(A.str2tree("4(2(3)(1))(6(5))"))



