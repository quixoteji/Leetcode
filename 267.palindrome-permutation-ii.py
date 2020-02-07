#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#

# @lc code=start
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        return self.sol1(s)

    def sol1(self, s) :
        counter = collections.Counter(s)
        odd = [char for (char, times) in counter.items() if times % 2 == 1]
        ans = []
        if len(odd) > 1 : return ans
        curr = odd[0] if odd else ''
        self.dfs(curr, counter, len(s), ans)
        return ans
        
    def dfs(self, curr, counter, n, ans):
        if len(curr) == n : 
            ans.append(curr)
            return 
        for char, times in counter.items() :
            if times >= 2 :
                counter[char] -= 2
                self.dfs(char + curr + char, counter, n, ans)
                counter[char] += 2
            

        
# @lc code=end

