#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, ans) :
        if not root : return
        ans.append(root.val)
        self.traverse(root.left, ans)
        self.traverse(root.right, ans)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans

        
# @lc code=end

