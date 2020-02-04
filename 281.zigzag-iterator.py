#
# @lc app=leetcode id=281 lang=python3
#
# [281] Zigzag Iterator
#

# @lc code=start
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.next = 1
        self.va = v1
        self.vb = v2

    def next(self) -> int:
        num = self.va.pop(0) if self.next > 0 else self.vb.pop(0)
        if self.va and self.vb : self.next *= -1
        elif not self.va : self.next = -1
        elif not self.vb : self.next = 1
        return num
        

    def hasNext(self) -> bool:
        return self.va and self.vb
        
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

