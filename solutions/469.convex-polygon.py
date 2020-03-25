#
# @lc app=leetcode id=469 lang=python3
#
# [469] Convex Polygon
#

# @lc code=start
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        return self.sol1(points)

    def sol1(self, points) :
        numPoints = len(points)
        prev, curr = 0, 0
        for idx in range(numPoints):
            dx1 = points[(idx+1)%numPoints][0] - points[idx][0]
            dy1 = points[(idx+1)%numPoints][1] - points[idx][1]
            dx2 = points[(idx+2)%numPoints][0] - points[idx][0]
            dy2 = points[(idx+2)%numPoints][1] - points[idx][1] 
            curr = dx1 * dy2 - dx2 * dy1
            if curr != 0:
                if curr * prev < 0 : return False
                else: prev = curr
        return True
   

# @lc code=end

