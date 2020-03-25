#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        return self.sol1(root)

    def sol1(self, root) :
        if not root : return []
        left = []
        right = []
        leaves = []
        self.helper(root, 0, left, right, leaves)
        return left + leaves + right[::-1]

    def helper(self, root, flag, left_boundary, right_boundary, leaves) :
        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root.val)
            return

        if flag == 0:
            left_boundary.append(root.val)
            self.helper(root.left, 1, left_boundary, right_boundary, leaves)
            self.helper(root.right, 2, left_boundary, right_boundary, leaves)
        elif flag == 1:
            left_boundary.append(root.val)
            if root.left:
                self.helper(root.left, 1, left_boundary, right_boundary, leaves)
                self.helper(root.right, 3, left_boundary, right_boundary, leaves)
            else:
                self.helper(root.right, 1, left_boundary, right_boundary, leaves)
        elif flag == 2:
            right_boundary.append(root.val)
            if root.right:
                self.helper(root.left, 3, left_boundary, right_boundary, leaves)
                self.helper(root.right, 2, left_boundary, right_boundary, leaves)
            else:
                self.helper(root.left, 2, left_boundary, right_boundary, leaves)
        else:
            self.helper(root.left, 3, left_boundary, right_boundary, leaves)
            self.helper(root.right, 3, left_boundary, right_boundary, leaves)
        

        
# @lc code=end

