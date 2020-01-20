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

    # Solution 2 : sliding window
    def sol2(self, s, t) :
        if not s or not t : return ''
        ans, minLen = '', len(s) + 1
        tDict = collections.defaultdict(int)
        for char in t : tDict[char] += 1
        left, tLen = 0, len(t)
        for right in range(len(s)) :
            char = s[right]
            tDict[char] -= 1
            if tDict[char] >= 0 : 
                tLen -= 1
            while tLen == 0 :
                if len(s[left : right + 1]) < minLen :
                    minLen = len(s[left : right + 1])
                    ans = s[left : right + 1]
                tDict[s[left]] += 1
                if tDict[s[left]] > 0 :
                    tLen += 1
                left += 1
        return ans


# @lc code=end

