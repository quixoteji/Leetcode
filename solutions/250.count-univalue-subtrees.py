#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def univalue(self, root) :
        if not root : return True
        # if not root.left and not root.right : return True
        if root.left and root.left.val != root.val : return False
        if root.right and root.right.val != root.val : return False
        return self.univalue(root.left) and self.univalue(root.right)

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root : return 0 
        count = 0
        queue = list()
        queue.append(root)
        while queue :
            l = len(queue)
            for i in range(l) :
                node = queue.pop(0)
                if self.univalue(node) : count += 1
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
        return count

        
# @lc code=end

