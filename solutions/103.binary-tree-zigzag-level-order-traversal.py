#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root : return root
        ans, level, direction = [], [], 1
        level.append(root)
        while level :
            nextlevel = []
            temp = []
            for node in level :
                temp.append(node.val)
                if node.left : nextlevel.append(node.left)
                if node.right : nextlevel.append(node.right)
            if direction == 1 : ans.append(temp[:])
            else : ans.append(temp[::-1])
            direction *= -1
            level = nextlevel[:]
        return ans
    
# @lc code=end

