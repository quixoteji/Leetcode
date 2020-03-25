#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for word in strs :
            groups[''.join(sorted(word))].append(word)
        return groups.values()
        
# @lc code=end

