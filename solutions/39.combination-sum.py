#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def helper(self, ans, curr, i , candidates, target) :
        if target == 0 : 
            ans.append(curr[:])
            return
        for s in range(i, len(candidates)) :
            if candidates[s] > target : return
            curr.append(candidates[s])
            self.helper(ans, curr, s, candidates, target - candidates[s]) 
            curr.pop()

        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        curr = []
        i = 0
        self.helper(ans, curr, i, candidates, target)
        return ans        
# @lc code=end

