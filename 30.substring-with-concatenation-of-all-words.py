#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def sol1(self, s, words) :
        ans = []
        hashmap_words = collections.defaultdict(int)
        if len(words) < 1 : return ans
        for word in words : hashmap_words[word] += 1
        subLen, wordLen, wordNum, idx = len(words) * len(words[0]), len(words[0]), len(words), 0 
        while idx + subLen <= len(s) :
            hashmap_sub = collections.defaultdict(int)
            substring = s[idx : idx + subLen]
            i = 0
            while i < wordNum :
                word = substring[i * wordLen : (i + 1) * wordLen]
                if hashmap_words[word] == 0 : break
                hashmap_sub[word] += 1
                if hashmap_sub[word] > hashmap_words[word] : break
                i += 1
            if i == wordNum : ans.append(idx)
            idx += 1
        return ans
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return self.sol1(s, words)
        
# @lc code=end

