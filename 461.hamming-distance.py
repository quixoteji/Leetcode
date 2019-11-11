#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        _sum = 0
        for i in range(32) :
            mask = 1 << i
            if (x & mask) ^ (y & mask) : _sum += 1
        return _sum
        
# @lc code=end

