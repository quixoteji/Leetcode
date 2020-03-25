#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        hashset = set(['a', 'e', 'i', 'o', 'u'])
        res = ''
        for char in s : 
            if char.lower() in hashset : res += char
        ans, res = list(s), res[::-1]
        i, j = 0, 0
        while i < len(ans) :
            if ans[i].lower() in hashset : 
                ans[i] = res[j] 
                j += 1
            i += 1
        return ''.join(ans)
# @lc code=end

