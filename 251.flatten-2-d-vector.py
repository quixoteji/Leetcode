#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#

# @lc code=start
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.vector = []
        for _v in v :
            self.vector += _v
        

    def next(self) -> int:
        return self.vector.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.vector) > 0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

