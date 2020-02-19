#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return self.sol1(points, K)

    def sol1(self, points, K) :
        return sorted(points, key = lambda x : x[0]**2 + x[1]**2)[:K]
        
# @lc code=end

