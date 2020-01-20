#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        return self.sol1(s)

    def sol1(self, s) :
        numStack, opStack = [], []
        flag = 0
        for i in range(len(s)) :
            if s[i].isspace() : 
                flag = 0
                continue
            elif s[i].isdigit() : 
                if flag : numStack[-1] = numStack[-1] + s[i]
                else : 
                    numStack.append(s[i])
                    flag = 1
            else :
                if s[i] in {'+', '-'} : opStack.append(s[i])
                else :
                    
                flag = 0
        
# @lc code=end

