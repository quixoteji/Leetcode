#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.sol1(nums)

    def sol1(self, nums) :
        if not nums : return [[]]
        bits = []
        self.dfs(bits, [], len(nums))
        ans = []
        for bit in bits :
            curr = []
            for i in range(len(bit)) :
                if bit[i] : curr.append(nums[i])
            ans.append(curr[:])
        return ans 
    
    def dfs(self, bits, curr, n) :
        if len(curr) == n : 
            bits.append(curr[:])
            return     
        for x in [0, 1] :
            curr.append(x)
            self.dfs(bits, curr, n)
            curr.pop()

     
# @lc code=end

