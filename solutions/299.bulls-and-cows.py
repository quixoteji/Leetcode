#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b, counter, hashset = 0, 0, collections.Counter(secret), set()
        for i in range(len(guess)) :
            if guess[i] == secret[i] : 
                a += 1
                counter[secret[i]] -= 1
                hashset.add(i)
        for i in range(len(guess)) :
            if i in hashset : continue
            if guess[i] in counter and counter[guess[i]] > 0:
                b += 1
                counter[guess[i]] -= 1
        return str(a) + 'A' + str(b) + 'B'
            
        
# @lc code=end

