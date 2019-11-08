#
# @lc app=leetcode id=422 lang=python3
#
# [422] Valid Word Square
#

# @lc code=start
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words : return True
        nums = [len(word) for word in words]
        hashset = set(nums)
        if len(hashset) != 1 or len(nums) != nums[0] : return False
        for i in range(len(words)) :
            s = ''
            for word in words :
                s += word[i]
            if s != words[i] : return False
        return True
        
# @lc code=end

