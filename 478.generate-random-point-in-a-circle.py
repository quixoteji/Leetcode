#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#

# @lc code=start
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        distance = self.radius ** 2 + 1
        while distance > self.radius ** 2:
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)
            distance = x ** 2 + y ** 2
        return [x + self.x, y + self.y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

