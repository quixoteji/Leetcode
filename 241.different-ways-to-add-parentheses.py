#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.sol1(input)

    def sol1(self, input) :
        ops = {
            '+' : lambda x, y : x + y,
            '-' : lambda x, y : x - y,
            '*' : lambda x, y : x * y
        }

        def ways(s) :
            ans = []
            for i in range(len(s)) :
                if s[i] in '+-*' :
                    ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
            if not ans: ans.append(int(s))
            return ans 
        return ways(input)


        
# @lc code=end

