#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()
        for house in houses :
            left, right = 0, len(heaters)
            while left < right :
                mid = left + (right - left) // 2
                if heaters[mid] < house : left = mid + 1
                else : right = mid
            dist1 = float('inf') if right == len(heaters) else heaters[right] - house
            dist2 = float('inf') if right == 0 else house - heaters[right - 1]
            res = max(res, min(dist1, dist2))
        return res
        
# @lc code=end

