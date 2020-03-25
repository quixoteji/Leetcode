#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums : return nums
        n = len(nums) * len(nums[0])
        if n != r * c or n // r != c : return nums 
        matrix = []
        for num in nums : matrix += num
        ans = [matrix[0 + c * i : c + c * i] for i in range(r)]
        return ans
        

        
# @lc code=end

