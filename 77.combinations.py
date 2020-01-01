#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:     
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]
        ans = []
        self.dfs(ans, [], nums, k, 0)
        return ans

    def dfs(self, ans, curr, nums, k, idx) :
        if len(curr) == k : 
            ans.append(curr[:])
            return
        for i in range(idx, len(nums)) :
            if nums[i] in curr : continue
            curr.append(nums[i])
            self.dfs(ans, curr, nums, k, i + 1)
            curr.pop()
        

        
# @lc code=end

