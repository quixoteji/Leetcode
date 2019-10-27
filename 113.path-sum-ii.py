#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, ans, curr, target, root):
        if root is None : return
        if root.left is None and root.right is None and target == root.val :
            curr.append(root.val)
            ans.append(curr[:])
            return
        curr.append(root.val)
        target = target - root.val
        self.dfs(ans, curr[:], target, root.left)
        self.dfs(ans, curr[:], target, root.right)
        


    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        self.dfs(ans, [], sum, root)
        return ans

        
# @lc code=end

