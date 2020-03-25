#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#

# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = list()
        self.size = size
        

    def next(self, val: int) -> float:
        self.window.append(val)
        if len(self.window) <= self.size : 
            return sum(self.window)/len(self.window) 
        else :
            self.window.pop(0)
            return sum(self.window) / self.size 


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end

