#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
        self.traverse(root.left, ans)
        self.traverse(root.right, ans)
        ans.append(root.val)
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans
        
# @lc code=end

