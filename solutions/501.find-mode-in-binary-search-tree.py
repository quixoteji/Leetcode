#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, hashmap) :
        if not root : return
        hashmap[root.val] += 1
        self.dfs(root.left, hashmap)
        self.dfs(root.right,hashmap)
    def findMode(self, root: TreeNode) -> List[int]:
        if not root : return None
        hashmap = collections.defaultdict(int)
        self.dfs(root, hashmap)
        l = sorted(list(hashmap.items()), key = lambda x : x[1])
        ans = []
        for key, value in l : 
            if value == l[-1][1] : ans.append(key)
        return ans
# @lc code=end

