#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        return self.sol2(root, p)

    def sol1(self, root, p) :
        if not root : return None
        ans = []
        self.inorder(root, ans)
        for i in range(len(ans)) :
            if ans[i].val == p.val and i < len(ans) - 1 :
                return ans[i + 1]
        return None

    def inorder(self, root, ans) :
        if not root : return
        self.inorder(root.left, ans)
        ans.append(root)
        self.inorder(root.right, ans)

    def sol2(self, root, p) :
        if p.right :
            p = p.right
            while p.left :
                p = p.left
            return p

        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')
        
        # inorder traversal : left -> node -> right
        while stack or root:
            # 1. go left till you can
            while root:
                stack.append(root)
                root = root.left
                
            # 2. all logic around the node
            root = stack.pop()
            if inorder == p.val:    # if the previous node was equal to p
                return root         # then the current node is its successor
            inorder = root.val
            
            # 3. go one step right
            root = root.right

        # there is no successor
        return None

            
                


        
# @lc code=end

