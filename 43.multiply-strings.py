#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1)) :
            int1 = ord(num1[i]) - ord('0')
            for j in range(len(num2)) :
                int2 = ord(num2[j]) - ord('0')

                tens, units = divmod(int1 * int2, 10)

                ans[i + j] += units
                if ans[i + j] > 9 :
                    ans[i + j + 1] += ans[i + j] // 10
                    ans[i + j] %= 10
                ans[i + j + 1] += tens
                if ans[i + j + 1] > 9 :
                    ans[i + j + 2] += ans[i + j + 1] // 10
                    ans[i + j + 1] %= 10 
        while len(ans) > 1 and ans[-1] == 0 : ans.pop()
        return "".join(map(str, ans[::-1]))        
# @lc code=end

