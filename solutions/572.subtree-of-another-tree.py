#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sameTree(self, s, t) :
        if not s and not t : return True
        elif (not s and t) or (s and not t) : return False
        else : return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s : return False
        if self.sameTree(s, t) : return True
        else : return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
# @lc code=end

