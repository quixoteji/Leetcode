#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 : return ''
        if len(strs) == 1 : return strs[0]
        ans = ''
        for char in strs[0] :
            temp = ans + char
            for str in strs[1:] :
                if not str.startswith(temp) :
                    temp = ''
                    break
            if temp :
                ans = temp
            else : 
                break
        return ans 

        
# @lc code=end

