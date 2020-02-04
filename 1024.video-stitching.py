#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#

# @lc code=start
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        return self.sol1(clips, T)

    def sol1(self, clips, T) : 
        clips.sort(key = lambda x : x[0])
        ans = prev = end = idx = 0
        
        while end < T :
            while idx < len(clips) and clips[idx][0] <= prev :
                end = max(end, clips[idx][1])
                idx += 1
            if prev == end : return -1
            prev = end 
            ans += 1

        return ans


# @lc code=end

