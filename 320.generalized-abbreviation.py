#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#

# @lc code=start
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        return self.sol1(word)

    def sol1(self, word) : 
        ans = []
        curr = ''
        flag = 0
        self.dfs(ans, curr, flag, 0, word) 
        return ans

    def dfs(self, ans, curr, flag, idx, word) :
        if idx == len(word) : 
            ans.append(curr)
            return 
        if flag == 1 : 
            self.dfs(ans, curr + word[idx], 0, idx + 1, word)
        else :
            for i in range(len(word) - idx + 1) :
                if i == 0 : self.dfs(ans, curr + word[idx], 0, idx + 1, word)
                else : self.dfs(ans, curr + str(i), 1, idx + i, word)
                
        
# @lc code=end

