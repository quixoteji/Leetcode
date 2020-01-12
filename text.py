import collections

class Solution:
    def minWindow(self, s, t):
        return self.sol2(s, t)

    # Solution 2 : sliding window(incorrect)
    def sol2(self, s, t) :
        if not s or not t: return ''
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
                    if hashmap[s[left]] > 0 : cnt -= 1
                    hashmap[s[left]] += 1
                left += 1
        return ans


A = Solution()
print(A.minWindow("bba", "ab"))

