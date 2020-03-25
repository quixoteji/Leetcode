#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 : limit the value range for subtrees
    def sol1(self, root) :
        return self.check(root, float('inf'), float('-inf'))

    def check(self, root, maxval, minval) :
        if not root : return True
        if root.val >= maxval or root.val <= minval : return False
        return self.check(root.left, root.val, minval) \
            and self.check(root.right, maxval, root.val)
    
    # Solution 2 : inorder traverse should be sorted
    prev = None
    def sol2(self, root) :
        return self.inorder(root)

    def inorder(self, root) :
        print(self.prev, root.val if root else - 100)
        if not root : return True
        if not self.inorder(root.left) : return False
        if self.prev is not None and root.val <= self.prev : return False
        self.prev = root.val
        return self.inorder(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.sol2(root)
        
# @lc code=end

