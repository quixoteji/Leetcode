#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        

    def addNum(self, val: int) -> None:
        if val not in self.list:
            bisect.insort(self.list, val)
        

    def getIntervals(self) -> List[List[int]]:
        ret = []
        curr = [self.list[0], self.list[0]]
        for i in range(1, len(self.list)):
            ele = self.list[i]
            if ele == curr[1] + 1:
                curr[1] = ele
            else:
                ret.append(curr)
                curr = [ele, ele]
        ret.append(curr)
        return ret
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

