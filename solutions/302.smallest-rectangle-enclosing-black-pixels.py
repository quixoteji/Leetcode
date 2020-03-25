#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#

# @lc code=start
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x + 1, len(image), False)
        left = self.searchColumns(image, 0, y, top, bottom, True)
        right = self.searchColumns(image, y + 1, len(image[0]), top, bottom, False)
        return (right - left) * (bottom - top)

    def searchRows(self, image, i, j, opt):
        while i != j:
            m = (i + j) // 2
            if ('1' in image[m]) == opt:
                j = m
            else:
                i = m + 1
        return i

    def searchColumns(self, image, i, j, top, bottom, opt):
        while i != j:
            m = (i + j) // 2
            if any(image[k][m] == '1' for k in range(top, bottom)) == opt:
                j = m
            else:
                i = m + 1
        return i
    
# @lc code=end

