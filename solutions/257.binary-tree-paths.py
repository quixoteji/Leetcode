#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, curr, res) :
        if root.left is None and root.right is None : 
            curr += str(root.val)
            res.append(curr[:])
        if root.left : self.dfs(root.left, curr+str(root.val)+'->', res)
        if root.right : self.dfs(root.right, curr+str(root.val)+'->', res)


    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        if not root : return ans
        self.dfs(root, '', ans)
        return ans

        
# @lc code=end

