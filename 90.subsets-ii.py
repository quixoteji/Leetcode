#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.sol1(nums)

    def sol1(self, nums) :
        nums.sort()
        res = []
        visited = set()
        self.dfs(res, [], len(nums))
        # print(res)
        ans = []
        for idx in res :
            temp = []
            for i in range(len(idx)) :
                if idx[i] : temp.append(nums[i])
            if tuple(temp[:]) in visited : continue
            else :
                visited.add(tuple(temp[:]))
                ans.append(temp[:])
        return ans

    def dfs(self, res, curr, k) :
        if k == len(curr) :
            res.append(curr[:])
            return
        for i in [0, 1] :
            curr.append(i)
            self.dfs(res, curr, k)
            curr.pop()
                 

# @lc code=end

