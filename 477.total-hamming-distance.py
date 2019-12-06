#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#

# @lc code=start
class Solution:    
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        hamming = 0
        for bit in range(32) :
            set_bits = 0
            for num in nums :
                set_bits += (num >> bit) & 1
            hamming += (n - set_bits) * set_bits
        return hamming
        
# @lc code=end

