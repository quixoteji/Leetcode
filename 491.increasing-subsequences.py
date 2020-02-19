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
        visited = set()
        self.dfs(ans, 0, [], nums, visited)
        return ans

    def dfs(self, ans, idx, curr, nums, visited) :
        if len(curr) > 1 and tuple(curr) not in visited: 
            ans.append(curr[:])
            visited.add(tuple(curr))
        for i in range(idx, len(nums)) :
            if not curr or nums[i] >= curr[-1] :
                curr.append(nums[i])
                self.dfs(ans, i+1, curr, nums, visited)
                curr.pop()

        
        


        
            


        
# @lc code=end

