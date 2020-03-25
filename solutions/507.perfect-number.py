#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0: return False
        hashset, k = set(), round(math.sqrt(num)) + 1

        for i in range(1, k) :
            if num % i == 0: 
                hashset.add(i)
                hashset.add(num//i)
        hashset.remove(num)

        return num == sum(hashset)

        
# @lc code=end

