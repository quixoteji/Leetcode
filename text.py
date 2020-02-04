import collections
import math

class Solution:
    def solve(self, s) :
        ans, num, sign, prev = 0, 0, '+', 1
        for i in range(len(s)) :
            char = s[i]
            if char.isdigit() :
                num = num * 10 + int(char)
            if char in ['+', '-', '*', '/'] or i == len(s) - 1 :
                if sign == '+' : 
                    ans += num
                    prev = num
                if sign == '-' : 
                    ans -= num
                    prev = num
                if sign == '*' : 
                    ans += prev * num
                    prev = num
                if sign == '/' : 
                    t = 1 if prev > 0 else -1
                    ans += abs(prev) // num * t
                    prev = num
                num = 0 
                sign = char
        return ans 

            
A = Solution()
print(A.solve("3+2*2"))
