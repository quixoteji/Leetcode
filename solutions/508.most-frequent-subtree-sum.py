#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        return self.sol1(root)
    
    # Solution 1 : dfs
    def sol1(self, root) :
        if not root : return []
        ans = []
        self.subtrees(ans, root)
        counter = collections.Counter(ans)
        ans = collections.defaultdict(list)
        for val in counter : ans[counter[val]].append(val)
        print(ans)
        return ans[max(ans.keys())]

    def subtrees(self, ans, root) :
        if not root : return 0
        val = self.subtrees(ans, root.left) + self.subtrees(ans, root.right) + root.val
        ans.append(val)
        return val


# @lc code=end

