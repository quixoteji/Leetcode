#
# @lc app=leetcode id=248 lang=python3
#
# [248] Strobogrammatic Number III
#

# @lc code=start
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        minLen, maxLen = len(low), len(high)
        low, high, count = int(low), int(high), 0
        strobo = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        live = [''] 
        next = ['0', '1', '8']
        if minLen == 1 : 
            count += sum([1 if low <= int(i) <= high else 0 for i in next])
        for i in range(2, maxLen + 1) :
            live = [s + num + strobo[s] for num in live for s in strobo]
            if minLen <= len(live[0]) <= maxLen :
                # print(live)
                # print([1 if num[0] != 0 and low <= int(num) <= high else 0 for num in live])
                count += sum([1 if str(int(num)) == num and low <= int(num) <= high else 0 for num in live])
            live, next = next, live
        
        return count


        
        
# @lc code=end

