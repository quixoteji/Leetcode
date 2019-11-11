#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        start = 0
        for i in range(len(path)) :
            if i == len(path) or path[i] == '/' :
                p = path[start : i - start]
                if p == '/' : continue
                if p == '..' :
                    if s : 
                        s.pop()
                    elif  len(p) > 0 and p != '.' :
                        s.append(p)
                start = i + 1
        
        ans = ''
        for i in range(len(s)) :
            ans += '/' + s[i]
        return "/" if not ans else ans
# @lc code=end

