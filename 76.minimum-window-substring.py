#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return self.sol2(s, t)

    # Solution 1 : brutal_force (time limit exceeded)
    def sol1(self, s, t) :
        # if s == t : return s
        ct = collections.Counter(t)
        for i in range(len(s)) :
            for j in range(len(s)) :
                if j + len(t) + i > len(s) : break
                ss = s[j : j + len(t) + i]
                css = collections.Counter(ss)
                flag = 1
                for char in ct :
                    if char not in css or css[char] < ct[char] : 
                        flag = 0
                        break
                if flag : return ss
        return ''

    # Solution 2 : sliding window(incorrect)
    def sol2(self, s, t) :
        hashmap = collections.defaultdict(int)
        for char in t : hashmap[char] += 1
        left = 0
        cnt, minLen, ans = 0, float('inf'), ''
        for i in range(len(s)) :
            if s[i] in hashmap :
                if hashmap[s[i]] > 0 : cnt += 1
                hashmap[s[i]] -= 1
            while cnt == len(t) :
                if i - left + 1 < minLen : 
                    minLen = i - left + 1
                    ans = s[left : i + 1]
                if s[left] in hashmap :
                    if hashmap[s[left]] <= 0 : cnt -= 1
                    hashmap[s[left]] += 1
                left += 1
        return ans
                


# @lc code=end

