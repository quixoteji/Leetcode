#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        return self.sol2(words)
    def sol2(self, words):
        map = {}
        letters = [0 for i in range(26)]  
        for i in range(len(words)):
            for j in range(len(words[i])):
                key=ord(words[i][j])-ord('a')
                letters[key]=0
                map[key]=set()
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            idx = 0
            for j in range(min(len(word1),len(word2))):
                if(word1[j]!=word2[j]):
                    key1 = ord(word1[j])-ord('a')
                    key2 = ord(word2[j])-ord('a')
                    count = letters[key2]
                    if(key2 not in map[key1]):
                        letters[key2] =count+1
                        map[key1].add(key2)
                    break
        dictionary = collections.deque()
        res = ''
        for i in range(26):
            if(letters[i]==0 and i in map):
                dictionary.appendleft(i)
        
        while(len(dictionary)!=0):
            nextup = dictionary.pop()
            res+=(chr(nextup+ord('a')))
            greaterSet = map[nextup]
            for greater in greaterSet:
                letters[greater]-=1
                if(letters[greater]==0):
                    dictionary.appendleft(greater)
        if(len(map)!=len(res)):
            return ""
        return res

    def sol1(self, words) :
        children = collections.defaultdict(set)
        parents = collections.defaultdict(set)
        characters = set()

        l = max([len(word) for word in words])

        for i in range(len(words)):
            for j in range(l) :
                if j < len(words[i]) :
                    characters.add(words[i][j])
                    if i > 0 and j < len(words[i - 1]) and words[i - 1][j] != words[i][j]:
                        children[words[i - 1][j]].add(words[i][j])
                    if i < len(words) - 1 and j < len(words[i + 1]) and words[i + 1][j] != words[i][j]:
                        parents[words[i + 1][j]].add(words[i][j])

        others = [char for char in characters if char not in parents and char not in children]
        others = ''.join(others)

        if len(others) == len(characters): return others

        node = [node for node in children if node not in parents]

        
        if len(node) != 1 : return ''
        ans = []
        self.dfs(node[0], children, len(characters) - len(others), ans)
        
        return ans[0] + others

    def dfs(self, curr, children, n, ans):
        if len(curr) == n :
            ans.append(curr)
            return
        for child in children[curr[-1]] :
            self.dfs(curr + child, children, n, ans)
            

# @lc code=end

