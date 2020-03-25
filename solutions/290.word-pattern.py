#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern) != len(str.split()) : return False
        hashtable = {}
        for i in range(len(pattern)) :
            if pattern[i] in hashtable :
                if hashtable[pattern[i]] != str.split()[i] : return False
            else :
                if str.split()[i] in hashtable.values() : return False
                hashtable[pattern[i]] = str.split()[i]
        return True
        
# @lc code=end

