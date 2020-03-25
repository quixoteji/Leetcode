#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        return self.sol2(s, k)

    # Solution 1 : brutal force
    def sol1(self, s, k) :
        if len(s) <= k : return len(s)
        mx = 0
        for i in range(len(s)) :
            for j in range(i, len(s)):
                t = s[i:j+1]
                if len(set(t)) <= k : mx = max(mx, len(t))
                else : break
        return mx

    # Solution 2 : sliding window
    def sol2(self, s, k) :
        if len(s) <= k : return len(s)
        mx = 0
        start = 0
        hashmap = collections.defaultdict(int)
        for i in range(len(s)) :
            hashmap[s[i]] += 1
            if len(hashmap) <= k : mx = max(mx, len(s[start : i+1]))
            while len(hashmap) > k :
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0 : del hashmap[s[start]]
                start = start + 1
        return mx
        
# @lc code=end

