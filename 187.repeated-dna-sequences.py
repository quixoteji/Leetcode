#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]: 
        if len(s) < 10 : return []
        idx = 0 
        hashset, ans = set(), set()
        while idx + 10 <= len(s):
            if s[idx : idx + 10] in hashset :
                ans.add(s[idx : idx + 10])
            else :
                hashset.add(s[idx : idx + 10])
            idx += 1
        return list(ans)

        
# @lc code=end

