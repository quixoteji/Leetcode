#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(x, y):
            #Using Euclid's algorithm - https://en.wikipedia.org/wiki/Greatest_common_divisor
            if x < y : 
                x, y = y, x
            while x != y and y != 0 :
                remainder = x % y 
                x = y
                y = remainder
            return x
        
        g = gcd(x,y)
        #print("gcd: ", g)
        if g == 0:
            return z == 0
        
        return (x+y) >= z and z % g == 0 
        
# @lc code=end

