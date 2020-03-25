#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        return self.sol2(root)

    # dfs : trival error
    def sol1(self, root) :
        if not root : return []
        indexes = collections.defaultdict(int)
        self.dfs(indexes, root, 0)
        ans = collections.defaultdict(list)
        for key, value in indexes.items() :
            ans[value].append(key)
        return [ans[v] for v in sorted(ans.keys())]

    def dfs(self, indexes, root, value) :
        if not root : return 
        indexes[root.val] = value
        if root.left : self.dfs(indexes, root.left, value - 1)
        if root.right : self.dfs(indexes, root.right, value + 1)

    # bfs 
    def sol2(self, root) :
        if not root : return []
        indexes = collections.defaultdict(list)
        queue = [[root, 0]]
        while queue :
            l = len(queue)
            for i in range(l) :
                node, value = queue.pop(0)
                indexes[value].append(node.val)
                if node.left : queue.append([node.left, value - 1])
                if node.right : queue.append([node.right, value + 1])
        return [indexes[v] for v in sorted(indexes.keys())]




        
# @lc code=end

