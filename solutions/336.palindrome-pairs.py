#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        return self.sol2(words)

    # Solution 1 : brutal force
    def sol1(self, words) :
        ans = []
        for i in range(len(words)) :
            for j in range(len(words)) :
                if i != j :
                    s = words[i] + words[j]
                    if s == s[::-1] : ans.append([i, j])
        return ans

    # Solution 2 :
    def sol2(self, words) :

        def prefixes(word) :
            ans = []
            for i in range(len(word)) :
                if word[i:] == word[i:][::-1] :
                    ans.append(word[:i])
            return ans

        def suffixes(word) :
            ans = []
            for i in range(len(word)) :
                if word[:i+1] == word[:i+1][::-1] :
                    ans.append(word[i+1:]) 
            return ans

        word_lookup = {word : i for i, word in enumerate(words)}
        ans = []

        for idx, word in enumerate(words):
            reverse = word[::-1]
            
            if reverse in word_lookup and idx != word_lookup[reverse] :
                ans.append([idx, word_lookup[reverse]])

            for s in suffixes(word) :
                rs = s[::-1]
                if rs in word_lookup :
                    ans.append([word_lookup[rs], idx])
            
            for p in prefixes(word) :
                rp = p[::-1]
                if rp in word_lookup :
                    ans.append([idx, word_lookup[rp]])

        return ans

        
# @lc code=end

