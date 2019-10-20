#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def sol1(self, s) :
        seen = set()
        maxlen, l, r = 0, 0, 0
        while l < len(s) and r < len(s) :
            if s[r] not in seen :
                seen.add(s[r])
                r += 1
                maxlen = max(maxlen, r - l)
            else : 
                seen.remove(s[l])
                l += 1
        
        return maxlen

    def sol2(self, s) :
        seen = {}
        longest, start = 0, 0
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start :
                start = seen[char] + 1
            longest = max(longest, i - start + 1)
            seen[char] = i
        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.sol2(s)

        
# @lc code=end

