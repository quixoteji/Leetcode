#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles : return False
        corners = set()
        area = 0
        for rec in rectangles :
            p1 = (rec[0], rec[1])
            p2 = (rec[0], rec[3])
            p3 = (rec[2], rec[1])
            p4 = (rec[2], rec[3])

            for p in [p1, p2, p3, p4]:
                if p not in corners : corners.add(p)
                else : corners.remove(p)
            
            area += (p4[0] - p1[0]) * (p4[1] - p1[1])
        if len(corners) != 4 : 
            return False
        p = sorted(list(corners), key = lambda x : (x[0], x[1]))
        return area == (p[-1][0] - p[0][0]) * (p[-1][1] - p[0][1])

# @lc code=end

