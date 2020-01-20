#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        return self.sol1(words)

    def sol1(self, words) :
        children = collections.defaultdict(set)
        parents = collections.defaultdict(set)
        characters = set()
        for word in words :
            for i in range(len(word)) :
                characters.add(word[i])
                if i < len(word) - 1 and word[i] != word[i + 1]: 
                    children[word[i]].add(word[i + 1])
                if i > 0 and word[i] != word[i - 1] :
                    parents[word[i]].add(word[i - 1])
        
        chars = [x for x in children if x not in parents]
        visited = set()
        s = ''
        for char in chars :
            visited.add(char)
            s += char
        ans = []
        self.dfs(ans, len(characters), s, visited)
        print(ans)
        return ''

    def dfs(self, ans, k, curr, visited) :
        

        
# @lc code=end

