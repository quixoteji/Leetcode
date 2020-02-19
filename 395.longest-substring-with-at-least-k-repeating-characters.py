#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.sol2(s, k)

    def sol1(self, s, k) :
        if not s : return 0
        ans = 0
        for i in range(len(s)) :
            for j in range(i, len(s)) :
                c = collections.Counter(s[i:j+1])
                flag = 1
                for v in c :
                    if c[v] < k :
                        flag = 0
                        break
                if flag and ans < len(s[i:j+1]) :
                    ans = len(s[i:j+1])
        return ans

    def sol2(self, s, k) :
        for char in set(s) :
            if s.count(char) < k :
                return max(self.sol2(t, k) for t in s.split(char))
        return len(s)


# @lc code=end

