#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = [p1, p2, p3, p4]
        hashmap = collections.defaultdict(int)
        for i in range(len(p)):
            for j in range(i + 1, len(p)) :
                distance = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                hashmap[distance] += 1
        
        return 0 not in hashmap.keys() and len(hashmap.keys()) == 2      

        
        
# @lc code=end

