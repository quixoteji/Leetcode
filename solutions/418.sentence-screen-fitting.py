#
# @lc app=leetcode id=418 lang=python3
#
# [418] Sentence Screen Fitting
#

# @lc code=start
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        return self.sol1(sentence, rows, cols)

    def sol1(self, sentence, rows, cols) :
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows) :
            start += cols - 1
            if s[start % len(s)] == ' ' :
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else :
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start // len(s)

        
# @lc code=end

