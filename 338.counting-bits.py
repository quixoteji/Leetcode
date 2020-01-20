#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        return self.sol1(num)

    def sol1(self, num) : 
        ans = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans

    def sol2(self, num) : 
        ans = [0 for _ in range(num + 1)]
        for i in range(1, num + 1) :
            if i % 2 == 0 : ans.append(ans[i // 2])
            else : ans.append(ans[i // 2] + 1)
        return ans
        
# @lc code=end

