#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    # Solution 1 : 2^n + time limit exceeded
    sol1_ans = 2**31 - 1
    def sol1(self, num, k) :
        if not num : return 0
        curr = ''
        k = len(num) - k
        if k == 0 : return '0'
        self.dfs(num, k, curr)
        return self.sol1_ans
    def dfs(self, num, k, curr) :
        if len(curr) + len(num) < k : return
        if len(curr) == k :
            if int(curr) < int(self.sol1_ans) : self.sol1_ans = str(int(curr))
            return
        self.dfs(num[1 : ], k, curr)
        self.dfs(num[1 : ], k, curr + num[0])

    # Solution 2 : monotone stack
    def sol2(self, num, k) :
        if k >= len(num) : return '0'
        ans = ''
        keep = len(num) - k
        for c in num :
            while k and ans and c < ans[-1] :
                ans = ans[:-1]
                k -= 1
            ans += c
        ans = ans[: keep]
        return str(int(ans)) if ans else '0'

    def removeKdigits(self, num: str, k: int) -> str:
        return self.sol2(num, k)
        
# @lc code=end

