#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#

# @lc code=start
class Solution:
    def dfs(self, ans, curr, even, odd) :

        


    def generatePalindromes(self, s: str) -> List[str]:
        ans = []
        even, odd = '', ''
        hashtable = collections.Counter(s)
        for key in hashtable:
            if hashtable[key] // 2 == 0 : even += key
            else : odd += key
        if len(odd) > 1 :
            return ans
        self.dfs(ans, curr, even, odd, hashtable)
        return ans

        
# @lc code=end

