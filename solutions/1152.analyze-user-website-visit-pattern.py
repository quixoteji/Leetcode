#
# @lc app=leetcode id=1152 lang=python3
#
# [1152] Analyze User Website Visit Pattern
#

# @lc code=start
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        freq = collections.defaultdict(set)
        for user, web in zip(username, website):
            freq[web].add(user)
        freq = [[web, len(user)] for web, user in freq.items() ]
        freq.sort(key = lambda x : (-x[1], x[0]))
        return [web for web, times in freq[:3]]
        
# @lc code=end

