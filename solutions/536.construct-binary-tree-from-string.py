#
# @lc app=leetcode id=536 lang=python3
#
# [536] Construct Binary Tree from String
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        return self.recursion(s)

    def recursion(self, s):
        idx = s.find('(')
        if idx < 0 : return TreeNode(int(s)) if s else None
        bal = 0
        for j, u in enumerate(s) :
            if u == '(': bal += 1
            if u == ')': bal -= 1
            if j > idx and bal == 0:
                break
        root = TreeNode(s[:idx])
        root.left = self.recursion(s[idx + 1 : j])
        root.right = self.recursion(s[j + 2 : -1])
        return root
    def linear(self, s):
        if not s : return None
        stack = []
        num = ''
        for i in range(len(s)) :
            if s[i].isdigit() or s[i] == "-":
                num += s[i]    
            elif num :
                node = TreeNode(int(num)) 
                if stack :
                    if not stack[-1].left :
                        stack[-1].left = node
                    else :
                        stack[-1].right = node
                else :
                    root = node
                if s[i] == '(' :
                    stack.append(node)
                num = ''
            elif s[i] == ')' :
                stack.pop()
            return root if num else TreeNode(int(num))




# @lc code=end

