#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.iterative(root, p, q)

    # Recursive Approach
    
    def recursive(self, root, p, q) :
        self.traverse(root, p, q)
        return self.ans
    
    def traverse(self, root, p, q) :
        if not root : return False
        left = self.traverse(root.left, p, q)
        right = self.traverse(root.right, p, q)
        mid = root == p or root == q
        if mid + left + right >= 2 : self.ans = root
        return mid or left or right

    # Iterative Approach
    def iterative(self, root, p, q) :
        stack = [root]
        parent = {root : None}
        while p not in parent or q not in parent :
            node = stack.pop()
            if node.left :
                parent[node.left] = node
                stack.append(node.left)
            if node.right :
                parent[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        while p : 
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors :
            q = parent[q]
        return q

    # Solution 1 : record path??????
    def sol1(self, root, p, q) :
        if not root : return None
        pPath = []
        qPath = []
        self.bfs(pPath, root, p)
        self.bfs(qPath, root, q)
        _pPath = [x.val for x in pPath]
        _qPath = [x.val for x in qPath]

        print(_pPath)
        print(_qPath)
        for node in qPath[::-1] :
            if node in pPath : return node
        return None

    def bfs(self, path, root, obj) :
        if root.val == obj.val : 
            path.append(obj)
            return 
        if root.left :
            path.append(root)
            self.bfs(path, root.left, obj)
            path.pop()
        if root.right :
            path.append(root)
            self.bfs(path, root.right, obj)
            path.pop()

        
# @lc code=end

