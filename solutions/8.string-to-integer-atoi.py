#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        ans = 0
        str = str.strip()
        s = str
        for i in range(len(str)) :
            if i == 0 and (str[i].isdigit() or str[i] == '+' or str[i] == '-') :
                continue
            if not str[i].isdigit() :
                s = str[:i]
                break

        print(s)
        try :
            ans = int(s)
        except :
            ans = 0

        if ans > 2**31 - 1 : return 2**31 - 1
        if ans < -1 * 2**31 : return -1 * 2**31
        
        return ans
# @lc code=end

