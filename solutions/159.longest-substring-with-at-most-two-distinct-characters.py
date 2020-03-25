#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#

# @lc code=start
class Solution:
    def brutal_force(self, s) :
        if len(s) < 2 : return len(s)
        maxLen = 0
        for i in range(len(s)) :
            for j in range(i + 1, len(s)) :
                if len(set(s[i : j + 1])) > 2 : break
                maxLen = max(maxLen, len(s[i : j + 1]))
        return maxLen
    def slidingWindow(self, s) :
        start, maxLen = 0, 0
        seen = dict()
        for i, char in enumerate(s) :
            if char in seen or len(seen) < 2 : 
                maxLen = max(maxLen, i - start + 1)
            else : 
                for key in seen :
                    if key != s[i - 1] :
                        start = seen[key] + 1
                        del seen[key]
                        break
            seen[char] = i
        return maxLen


    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return self.slidingWindow(s)
        
# @lc code=end

