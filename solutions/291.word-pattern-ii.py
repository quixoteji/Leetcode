#
# @lc app=leetcode id=291 lang=python3
#
# [291] Word Pattern II
#

# @lc code=start
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self.sol1(pattern, str)

    # Solution 1 : dfs
    def sol1(self, pattern, str) :
        return self.match(pattern, str, dict())

    def match(self, pattern, str, dictionary) :
        if len(pattern) == 0 : return len(str) == 0
        for end in range(1, len(str) - len(pattern) + 2) :
            if pattern[0] not in dictionary and str[:end] not in dictionary.values() :
                dictionary[pattern[0]] = str[:end]
                if self.match(pattern[1:], str[end:], dictionary) :
                    return True
                del dictionary[pattern[0]]
            elif pattern[0] in dictionary and dictionary[pattern[0]] == str[:end] :
                if self.match(pattern[1:], str[end:], dictionary) :
                    return True
        return False

        
# @lc code=end

