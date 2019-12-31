#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return self.sol1(words)

    def sol1(self, words) :
        if not words : return 0
        bits = [0 for word in words]
        sorted(words, key = lambda word : len(word), reverse = True)
        for i in range(len(words)) :
            c = collections.Counter(words[i])
            for key in c.keys():
                bits[i] += 1 << (ord(key) - ord('a'))
        ans = []
        for i in range(len(words)) :
            for j in range(i + 1, len(words)) :
                if bits[i] & bits[j] == 0 : 
                    ans.append(len(words[i]) * len(words[j]))
        return max(ans) if ans else 0

        
        
# @lc code=end

