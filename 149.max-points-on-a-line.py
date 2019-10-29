#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2: return len(points)
        htable = collections.defaultdict(set)
        for i in range(len(points)) :
            for j in range(i + 1, len(points)) :
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 - x2 == 0 : 
                    a = float('inf')
                    b = x1
                else :
                    a = (y1 - y2) / (x1 - x2)
                    b = y1 - a * x1
                htable[(a, b)].add((x1, y1))
                htable[(a, b)].add((x2, y2))
        maxVal = 0
        for value in htable.values():
            maxVal = max(maxVal, len(value))
        return maxVal

        
# @lc code=end

