#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = list()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min: self.min.append(x)
        else :
            if x <= self.min[-1]: self.min.append(x)

    def pop(self) -> None:
        temp = self.stack.pop()
        if self.min[-1] == temp : self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

