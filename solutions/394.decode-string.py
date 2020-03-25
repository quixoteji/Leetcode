#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        return self.sol1(s)

    # Solution 1 :
    def sol1(self, s) :
        if not s : return ''
        stack = []
        curNum, curS = 0, ''
        for c in s :
            if c == '[' :
                stack.append(curS)
                stack.append(curNum)
                curS, curNum = '', 0
            elif c == ']' :
                num = stack.pop()
                prevS = stack.pop()
                curS = prevS + num * curS
            elif c.isdigit() :
                curNum = curNum * 10 + int(c)
            else : 
                curS += c
        return curS

        

        
# @lc code=end

