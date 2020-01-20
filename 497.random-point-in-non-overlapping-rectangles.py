#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#

# @lc code=start
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.psum = []
        self.tot = 0
        for rect in rects :
            self.tot += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.psum.append(self.tot)

    def pick(self) -> List[int]:
        target = random.randint(0, self.tot - 1)
        l, h = 0, len(self.rects) - 1
        while l != h :
            mid = (l + h) // 2
            if target >= self.psum[mid] : l = mid + 1
            else: h = mid
        x = self.rects[l]
        width = x[2] - x[0] + 1
        height = x[3] - x[1] + 1
        base = self.psum[l] - width * height
        return [x[0] + (target - base) % width, x[1] + (target - base) // width]
            




# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

