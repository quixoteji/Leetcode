#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 1 : return int(num) in [0, 1, 8]
        hashmap = {'1' : '1',  '0' : '0', '6' : '9', '8' : '8', '9' : '6'}
        s = ''
        for char in num :
            if char in hashmap :
                s += hashmap[char]
            else :
                s += char
        return s == num[::-1]
        
        
# @lc code=end

