#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def sol1(self, root) :
        ans = []
        self.traverse(root, ans)
        return ans

    def traverse(self, root, ans) :
        if not root : return 
        self.traverse(root.left, ans)
        ans.append(root.val)
        self.traverse(root.right, ans)

    # Solution 2 : iteration
    def sol2(self, root) :
        ans = []
        stack, curr = [], root
        while curr or stack :
            while curr : 
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.sol2(root)
        
# @lc code=end

