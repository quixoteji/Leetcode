#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        num_A = 0
        for i, char in enumerate(s) :
            if char == 'A' : num_A += 1
            if num_A > 1 : return False
            if char == 'L' and i > 1 and s[i] == s[i - 1] and s[i - 1] == s[i - 2] : 
                return False
        return True
        
# @lc code=end

