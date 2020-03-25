#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def level_traverse(self, root) :
        if not root : return []
        ans = []
        queue = []
        queue.append(root)
        while queue :
            # print(len(queue))
            qLen = len(queue)
            ans.append(queue[-1].val)
            for i in range(qLen) :
                node = queue.pop(0)
                if node.left : queue.append(node.left)
                if node.right : queue.append(node.right)
        return ans

    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.level_traverse(root)
        
# @lc code=end

