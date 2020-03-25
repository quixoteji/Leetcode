#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = collections.Counter(s)
        ans = n = len(s)
        start = 0
        for i, char in enumerate(s) :
            cnt[char] -= 1
            while start < n and all(n // 4 >= cnt[c] for c in 'QWER') :
                ans = min(ans, i - start + 1)
                cnt[s[start]] += 1
                start = start + 1
        return ans


        
# @lc code=end

