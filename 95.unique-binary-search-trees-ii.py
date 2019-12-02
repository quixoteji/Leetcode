#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Solution 1 : recursion
    def sol1(self, n) :
        return self.gen(1, n) if n else []

    def gen(self, start, end) :
        if start > end : return [None]
        all_trees = []
        for i in range(start, end + 1) :
            left = self.gen(start, i - 1)
            right = self.gen(i + 1, end)
            for l in left :
                for r in right :
                    curr = TreeNode(i)
                    curr.left, curr.right = l, r
                    all_trees.append(curr)
        return all_trees


    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.sol1(n)
        
# @lc code=end

