#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I' : 1, 'V' : 5, 'X' : 10, 
                    'L' : 50, 'C' : 100, 'D' : 500, 
                    'M' : 1000}
        
        ans = hashmap[s[0]] 
        for i in range(1, len(s)) :
            ans += hashmap[s[i]]
            if hashmap[s[i]] > hashmap[s[i - 1]] : 
                ans -= 2 * hashmap[s[i - 1]]
        
        return ans

        
# @lc code=end

