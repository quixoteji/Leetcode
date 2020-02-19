#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        return self.recursion(root)

    def recursion(self, root) :
        if root :
            self.recursion(root.right)
            self.ans += root.val
            root.val = self.ans
            self.convertBST(root.left)
        return root

    def iteration(self, root) :
        total = 0
        node = root
        stack = []
        while stack or node :
            while node :
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root

        

        
        
        
# @lc code=end

