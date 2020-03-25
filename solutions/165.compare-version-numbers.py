#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        while len(v1) < len(v2) :
            v1.append(0)
        while len(v1) > len(v2) :
            v2.append(0)
        for n1, n2 in zip(v1, v2) :
            if n1 > n2 : return 1
            if n1 < n2 : return -1
        return 0
        
# @lc code=end

