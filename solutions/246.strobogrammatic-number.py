#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#

# @lc code=start
class Solution:
    def isStrobogrammatic(self, num: str) -> bool: 
        if not num : return True
        hashmap = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        
        l, r = 0, len(num) - 1
        while l <= r :
            if num[l] not in hashmap or hashmap[num[l]] != num[r] : return False
            l, r = l + 1, r - 1
        return True
        
# @lc code=end

