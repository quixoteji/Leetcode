#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        return self.sol1(root)

    def sol1(self, root) :
        if not root : return []
        ans = []
        while root :
            temp = []
            root = self.remove(root, temp)
            ans.append(temp[:])
        return ans

    def remove(self, root, temp) :
        if not root : return None
        if not root.left and not root.right : 
            temp.append(root.val)
            return None
        root.left = self.remove(root.left, temp)
        root.right = self.remove(root.right, temp)
        return root        
# @lc code=end

