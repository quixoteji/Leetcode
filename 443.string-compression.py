#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2 : return len(chars)
        p1, p2, num = 0, 1, 1
        while p2 < len(chars) :
            if chars[p2] == chars[p1] :
                num += 1
            else :
                if num > 1 : 
                    p1 += 1
                    nums = list(str(num))
                    for num in nums :
                        chars[p1] = num
                        p1 += 1
                num = 1
            p2 += 1
        if num > 1 : 
            p1 += 1
            nums = list(str(num))
            for num in nums :
                chars[p1] = num
                p1 += 1
        return p1

        
# @lc code=end

