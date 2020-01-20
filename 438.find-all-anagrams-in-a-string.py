#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.sol3(s, p)

    # Solution 1 : brutal force
    def sol1(self, s, p) :
        ans = []
        cp = collections.Counter(p)
        for i in range(len(s) - len(p) + 1) :
            t = s[i : i + len(p)]
            ct = collections.Counter(t)
            if cp == ct : ans.append(i)
        return ans

    # Solution 2 : 
    def sol2(self, s, p) :
        if not s : return []
        ans = []
        cnt = [0 for _ in range(128)]
        for char in p : cnt[ord(char) - ord('a')] += 1
        i = 0
        while i < len(s) - len(p) + 1 :
            tmp = cnt[:]
            success = True
            for j in range(i, i + len(p)):
                char = ord(s[j]) - ord('a')
                tmp[char] -= 1
                if tmp[char] < 0 : 
                    success = False
                    break
            if success : ans.append(i)
            i += 1
        return ans
    # Solution 3 : sliding window
    def sol3(self, s, p) :
        if not s : return []
        ans = []
        cs = collections.Counter(s[:len(p)-1])
        cp = collections.Counter(p)
        for i in range(len(p)-1,len(s)):
            cs[s[i]] += 1   # include a new char in the window
            if cs == cp:    # This step is O(1), since there are at most 26 English letters 
                ans.append(i-len(p)+1)   # append the starting index
            cs[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if cs[s[i-len(p)+1]] == 0: 
                del cs[s[i-len(p)+1]]   # remove the count if it is 0
        return ans

    
# @lc code=end

