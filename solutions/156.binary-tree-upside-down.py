#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def iteration(self, root) :
        curr, prev, next, temp = root, None, None, None
        while curr :
            next = curr.left
            curr.left = temp
            curr.rigth = prev
            prev, curr = curr, next
        return prev

    def recursion(self, root) :
        if not root or not root.left : return root
        left, right = root.left, root.right
        node = self.recursion(left)
        left.left, left.right = right, root
        root.left, root.right = None, None
        return node


    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        return self.recursion(root)

        
# @lc code=end

