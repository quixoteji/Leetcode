#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = []
        w = 1
        while w * w <= area :
            if area % w == 0 : res.append([area // w, w])
            w += 1
        return res[-1]

        

        
# @lc code=end

