#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.bfs(root, k)

    def dfs(self, root, k) :
        def inorder(root) :
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)[k - 1]

    def bfs(self, root, k) :
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
# @lc code=end

