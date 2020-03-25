#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        return self.sol2(s)

    def sol1(self, s) :
        num, sign, stack = 0, '+', []
        for i in range(len(s)) : 
            char = s[i]
            if char.isdigit() : 
                num = num * 10 + int(char)
            if char in ['+', '-', '*', '/'] or i == len(s) - 1 :
                if sign == '+' :
                    stack.append(num)
                if sign == '-' :
                    stack.append(-num)
                if sign == '*' :
                    stack.append(stack.pop() * num)
                if sign == '/' :
                    sign = 1 if stack[-1] > 0 else -1
                    stack.append(abs(stack.pop()) // num * sign)
                num = 0
                sign = char
        return sum(stack)
                    

            

        
# @lc code=end

