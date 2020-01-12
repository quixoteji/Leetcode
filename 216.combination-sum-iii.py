#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.sol1(k, n)

    def sol1(self, k, n) : 
        nums = [i + 1 for i in range(9)]
        ans = []
        self.dfs(ans, [], nums, k, n, 0)
        return ans

    def dfs(self, ans, curr, nums, k, n, idx) :
        if len(curr) == k and sum(curr) == n :
            ans.append(curr[:])
            return 
        if len(curr) > k : return
        for i in range(idx , len(nums)) :
            curr.append(nums[i])
            self.dfs(ans, curr, nums, k, n, i + 1)
            curr.pop()

        
# @lc code=end

