#
# @lc app=leetcode id=1167 lang=python3
#
# [1167] Minimum Cost to Connect Sticks
#

# @lc code=start
from heapq import heapify, heappop, heappush

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks: return 0
        heapify(sticks)
        ans = 0
        while len(sticks) > 1 :
            first = heappop(sticks)
            second = heappop(sticks)
            cost = first + second
            heappush(sticks, cost)
            ans += cost
        return ans

        
# @lc code=end

