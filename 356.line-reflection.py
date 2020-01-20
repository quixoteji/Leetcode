#
# @lc app=leetcode id=356 lang=python3
#
# [356] Line Reflection
#

# @lc code=start
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        return self.sol1(points)

    def sol1(self, points) :
        hashset = set()
        mx, mn = float('-inf'), float('inf')
        for p in points :
            mx = max(p[0], mx)
            mn = min(p[0], mn)
            hashset.add(tuple(p))
            
        y = (mx + mn) / 2
        
        for p in points :
            rp = [0,0]
            rp[1] = p[1]
            rp[0] = y - (p[0] - y)
            
            if tuple([rp[0], rp[1]]) not in hashset : return False
        return True

        
# @lc code=end

