#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.bfs(root, sum)

        

    def bfs(self, root, sum) :
        if not root : return 0
        
        stack = [root]
        paths = {root : [root.val]}
        ans = 0
        while stack :
            l = len(stack)
            for i in range(l) :
                node = stack.pop()
                for ele in paths[node] : ans += 1 if ele == sum else 0
                
                tmp = paths[node]
                if node.left :
                    tmpLeft = [x + node.left.val for x in tmp]
                    tmpLeft.append(node.left.val)
                    paths[node.left] = tmpLeft
                    stack.append(node.left)
                if node.right :
                    tmpRight = [x + node.right.val for x in tmp]
                    tmpRight.append(node.right.val)
                    paths[node.right] = tmpRight
                    stack.append(node.right)
        return ans
                

        
# @lc code=end

