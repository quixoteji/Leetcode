#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p1 in points :
            hashtable = collections.defaultdict(int)
            for p2 in points :
                hashtable[(p1[0]-p2[0])**2 + (p1[1]-p2[1])**2] += 1
            for key in hashtable :
                res += hashtable[key] * (hashtable[key] - 1)
        return res
        
# @lc code=end

