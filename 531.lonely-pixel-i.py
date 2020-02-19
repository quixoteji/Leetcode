#
# @lc app=leetcode id=531 lang=python3
#
# [531] Lonely Pixel I
#

# @lc code=start
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        return self.sol1(picture)

    def sol1(self, picture) :
        m, n = len(picture), len(picture[0])
        rowTable, colTable = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(m) :
            for j in range(n) :
                if picture[i][j] == 'B' :
                    rowTable[i] += 1
                    colTable[j] += 1
                    

        
# @lc code=end

