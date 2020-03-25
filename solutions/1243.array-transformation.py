#
# @lc app=leetcode id=1243 lang=python3
#
# [1243] Array Transformation
#

# @lc code=start
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        return self.sol1(arr)

    def sol1(self, arr) :
        P, C = None, arr
        while P != C :
            P, C = C, C[:]
            for i in range(1, len(C) - 1) :
                C[i] += int(P[i-1] > P[i] < P[i+1]) - int(P[i-1] < P[i] > P[i+1])
        return P
        
# @lc code=end

