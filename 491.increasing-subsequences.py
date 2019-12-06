#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums : return []
        ans = []
        curr = []
        self.dfs(ans, curr, nums)
        
# @lc code=end

