#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        # strip spaces
        s = s.strip()
        # Check one or less
        if len(s) < 1 : return False
        if len(s) == 1 : return s.isdigit()
        # check non digits
        c = collections.Counter(s)
        digit = 0
        for char in c :
            if not char.isdigit() :
                if char not in ['-', '+', '.', 'e'] :
                    return False
                elif c['e'] > 1 or c['.'] > 1 or c['+'] > 2 or c['+'] > 2:
                    return False
                else :
                    continue
            else : 
                digit += 1
        if digit == 0 : return False
        # check e :
        if 'e' in s :
            pre, post = s.split('e')

            if ('-' in pre and pre[0] != '-') or ('+' in pre and pre[0] != '+') :
                return False

            if ('-' in post and post[0] != '-') or ('+' in post and post[0] != '+') :
                return False

            if (len(pre) < 1 or len(post) < 1) :
                return False

            if len(pre) == 1 and (pre[0] in ['-', '+', '.']) :
                return False

            if  len(post) == 1 and (post[0] in ['-', '+', '.']) :
                return False
            if '.' in post : 
                return False
        else :
            if c['+'] > 1 or c['-'] > 1 : return False
            if ('-' in s and s[0] != '-') or ('+' in s and s[0] != '+') :
                return False


        return True
        
# @lc code=end

