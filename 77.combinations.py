#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def dfs(self, ans, curr, nums, idx, k) :
        if len(curr) == k : 
            ans.append(curr[:])
            return
        for num in nums[idx : ]:
            curr.append(num)
            self.dfs(ans, curr, nums, idx + 1, k)
            curr.pop()
        

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        ans, curr = [], []
        self.dfs(ans, curr, nums, 0, k)
        return ans
        

        
# @lc code=end

