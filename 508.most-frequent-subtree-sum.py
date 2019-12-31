#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        return self.sol1(root)
    
    # Solution 1 : dfs
    def sol1(self, root) :
        if not root : return None
        ans = []
        self.dfs(root, ans)

# @lc code=end

