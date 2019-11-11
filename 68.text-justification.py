#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        width = 0
        line = []
        for word in words :
            if width + len(word) <= maxWidth :
                line.append(word)
                width += len(word) + 1
            else :
                lines.append(line)
                line = [word]
                width = len(word) + 1
        if line : lines.append(line)
        
        ans = []
        for line in lines[:-1] :
            _sum = sum([len(word) for word in line])
            _num = len(line)
            t = ''
            if _num - 1 == 0 :
                t += line[0] + ' ' * (maxWidth - len(line[0]))
            else :
                _average, _extra = divmod(maxWidth - _sum, _num - 1)
                for i in range(_num - 1) :
                    if _extra > 0 :
                        t += line[i] + ' ' * (_average + 1)
                        _extra -= 1
                    else : t += line[i] + ' '*_average
                t += line[-1]
            ans.append(t)

        t = ''
        n = maxWidth
        for word in lines[-1][:-1] :
            t += word + ' '
            n -= len(word) + 1
        t += lines[-1][-1] + ' ' * (n - len(lines[-1][-1]))
        ans.append(t)
        return ans



# @lc code=end

