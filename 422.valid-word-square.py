#
# @lc app=leetcode id=422 lang=python3
#
# [422] Valid Word Square
#

# @lc code=start
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ref = []
        for i in range(len(words)):
            tmp = ''
            for word in words :
                if i < len(word) : tmp += word[i]
            ref.append(tmp)
        return words == ref

# @lc code=end

