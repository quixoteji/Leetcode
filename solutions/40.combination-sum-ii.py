#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def dfs(self, ans, curr, i, candidates, target) :
        if target == 0 : 
            ans.append(curr[:])
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1] : continue
            if candidates[j] > target : return
            curr.append(candidates[j])
            self.dfs(ans, curr, j + 1, candidates, target - candidates[j])
            curr.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        curr = []
        i = 0
        self.dfs(ans, curr, i, candidates, target)
        return ans
        
# @lc code=end

