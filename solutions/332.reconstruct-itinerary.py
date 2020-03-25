#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        return self.solution1(tickets)

    def solution1(self, tickets) :
        dt = collections.defaultdict(list)
        tickets.sort(reverse=True)
        for s, e in tickets : dt[s].append(e)
        rst, stack = [], ['JFK']
        while stack :
            while dt[stack[-1]] :
                stack.append(dt[stack[-1]].pop())
            rst.append(stack.pop())
        rst.reverse()
        return rst


        
# @lc code=end

