#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)
        for char in ransomNote :
            if char not in counter : return False
            if counter[char] == 0 : return False
            counter[char] -= 1
        return True
        
# @lc code=end

