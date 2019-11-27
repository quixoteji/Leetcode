#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

# @lc code=start
class Solution:
    def sol1(self, strings) :
        hashmap = collections.defaultdict(list)
        for s in strings : 
            key = '0'
            if len(s) > 1 :
                for i in range(1, len(s)) :
                    num = ord(s[i]) - ord(s[i-1])
                    key += str(num) if num > 0 else str(num + 26)
            hashmap[key].append(s)
        return list(hashmap.values())

    def sol2(self, strings) :
        shifted  = collections.defaultdict(list)
        for s in strings :
            shift = ord(s[0]) - ord('a')
            s_shifted = ''.join([chr(((ord(c) - ord('a') - shift) % 26) + ord('a')) for c in s])
            shifted[s_shifted].append(s)
        return shifted.values()


    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        return self.sol2(strings)
        
# @lc code=end

