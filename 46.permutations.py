#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def dfs(self, ans, visited, nums) :
        if len(visited) == len(nums) :
            # temp = visited[:]
            # ans.append(temp)
            ans.append(visited[:])
            return 
        for num in nums :
            if num in visited : continue
            else :
                visited.append(num)
                self.dfs(ans, visited, nums)
                visited.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = []
        self.dfs(ans, visited, nums)
        return ans
        
# @lc code=end

