#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(x) :
            if x != U[x][0] :
                px, pv = find(U[x][0])
                U[x] = (px, U[x][1] * pv)
            return U[x]

        def divide(x, y) :
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry: return -1.0
            return vx / vy

        U = {}
        for (x, y), val in zip(equations, values):
            if x not in U and y not in U :
                U[x], U[y] = (y, val), (y, 1.0)
            elif x not in U :
                U[x] = (y, val)
            elif y not in U :
                U[y] = (x, 1.0/val)
            else :
                rx, vx = find(x)
                ry, vy = find(y)
                U[rx] = (ry, val / vx * vy)
        ans = [divide(x, y) if x in U and y in U else -1 for x, y in queries]
            
        return ans
        
# @lc code=end

