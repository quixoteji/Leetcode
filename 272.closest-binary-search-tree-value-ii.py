#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        return self.sol1(root, target, k)


    def sol2(self, root, target, k) :
        ans = []
        preStack = []
        sucStack = []
        while root :
            if root.val < target :
                preStack.append(root)
                root = root.right
            else :
                sucStack.append(root)
                root = root.left

        def getPre(stack) :
            if stack :
                pre = stack.pop()
                p = pre.left
                while p :
                    stack.append(p)
                    p = p.right
                return pre

        def getSuc(stack) :
            if stack :
                suc = stack.pop()
                p = suc.right
            while p :
                stack.append(p)
                p = p.left

        pre = getPre(preStack)
        suc = getSuc(sucStack)

        while len(ans) < k : 
            if pre and not suc :
                ans.append(pre.val)
                pre = getPre(preStack)
            elif not pre and suc :
                ans.append(suc.val)
                suc = getSuc(sucStack)
            elif pre and suc and abs(pre.val - target) <= abs(suc.val - target):
                ans.append(pre.val)
                pre = getPre(preStack)
            else:
                ans.append(suc.val)
                suc = getSuc(sucStack)

        return ans



    def sol1(self, root, target, k) :
        ans = []
        self.dfs(ans, root)
        if target <= ans[0] : return ans[0:k]
        if target >= ans[-1] : return ans[-k:]
        idx = 0
        for i in range(len(ans)) :
            if ans[i] == target :
                idx = i
                break
            if i > 0 and ans[i - 1] < target < ans[i] :
                idx = i if abs(target - ans[i]) < abs(target - ans[i-1]) else i - 1
                break
        print(ans)
        print(idx)
        res = [ans[idx]]
        l, r = idx - 1, idx + 1 
        while len(res) < k :
            if l < 0 : idx, r = r, r + 1
            elif r > len(ans) - 1 : idx, l = l, l - 1
            elif abs(target - ans[l]) < abs(target - ans[r]) : idx, l = l, l - 1
            else : idx, r = r, r + 1
            res.append(ans[idx])
        return res

    def dfs(self, ans, root) :
        if not root : return
        self.dfs(ans, root.left)
        ans.append(root.val)
        self.dfs(ans, root.right)

            


        
# @lc code=end

