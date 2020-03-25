#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3 : return len(points)
        max_count = 1
        for point in points :
            max_count = max(self.points_on_line(point, points), max_count)
        return max_count

    def points_on_line(self, point, points) :
        duplicate = 0
        vertical = 0
        horizontal = 0
        slope = collections.defaultdict(int)
        for p in points :
            if p[0] == point[0] and p[1] == point[1] :
                duplicate += 1
            elif p[0] == point[0] : 
                horizontal += 1
            elif p[1] == point[1] :
                vertical += 1
            else :
                s = (p[0] - point[0]) / (p[1] - point[1])
                slope[s] += 1
        max_slope = max(slope.values()) if slope.values() else 0
        max_count = max(horizontal, vertical, max_slope)
        return max_count + duplicate
            

        

        
# @lc code=end

