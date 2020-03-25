#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    hashmap = {'(' : ')', '[' : ']', '{' : '}'}
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s :
            if char in ['(', '[', '{'] :
                stack.append(self.hashmap[char])
            else :
                if len(stack) == 0 or stack.pop() != char : 
                    return False
                
        return len(stack) == 0
# @lc code=end

