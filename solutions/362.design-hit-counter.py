#
# @lc app=leetcode id=362 lang=python3
#
# [362] Design Hit Counter
#

# @lc code=start
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(int)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.data[timestamp] += 1

        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # print(self.data)
        interval = [max(0, timestamp - 300), timestamp]
        # print(interval)
        ans = 0
        for key in self.data.keys():
            if interval[0] < key <= interval[1]:
                # print(key)
                ans += self.data[key]
        return ans
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
# @lc code=end

