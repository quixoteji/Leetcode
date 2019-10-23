#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def dfs(self, ans, visited, curr, nums) :
        if len(curr) == len(nums) :
            ans.append(curr[:])
            return
        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i-1] : continue
            if i in visited : continue
            visited.append(i)
            curr.append(nums[i])
            self.dfs(ans, visited, curr, nums)
            curr.pop()
            visited.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        visited = []
        curr = []
        self.dfs(ans, visited, curr, nums)
        return ans
        
# @lc code=end

