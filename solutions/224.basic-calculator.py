#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        return self.sol1(s)

    def sol1(self, s) :
        ans, num, sign, stack = 0, 0, 1, []
        for char in s :
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in ['-', '+'] :
                ans += num * sign
                num = 0
                sign = [-1, 1][char == '+']
            elif char == '(' :
                stack.append(ans)
                stack.append(sign)
                ans, num, sign = 0, 0, 1
            elif char == ')' :
                ans += sign * num
                ans *= stack.pop()
                ans += stack.pop()
                num = 0
            else :
                continue
        return ans + sign * num


        


        
# @lc code=end

