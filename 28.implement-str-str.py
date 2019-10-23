#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "" : return 0
        p1 = p2 = 0
        while p1 < len(haystack) and p1 + p2 < len(haystack): 
            if haystack[p1 + p2] == needle[p2] : 
                p2 += 1
                if p2 == len(needle) : return p1
            else : 
                p2 = 0
                p1 += 1
            
        return -1 
# @lc code=end

