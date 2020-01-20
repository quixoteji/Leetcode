#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = [x for x in path.split('/') if x]
        ans = []
        for item in s :
            if item == '.' : continue
            elif item == '..' :
                if len(ans) > 0 : ans.pop()
                else : continue
            else :
                ans.append(item)
        if len(ans) == 0 : res = '/'
        else : res = '/' + '/'.join(ans)
        return res
# @lc code=end

