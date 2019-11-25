#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack, ops = list(), {'+', '-', '*', '/'}
        for char in tokens :
            if char not in ops : 
                num_stack.append(int(char))
            else :
                b = num_stack.pop()
                a = num_stack.pop()
                if char == '+' : c = a + b
                elif char == '-' : c = a - b
                elif char == '*' : c = a * b
                else : c = int(a / b)
                num_stack.append(c)
        return num_stack.pop()
        
# @lc code=end

