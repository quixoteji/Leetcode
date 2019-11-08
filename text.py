import collections

class Solution:
    def findLHS(self, nums) :
        if not nums: return 0
        counter = collections.Counter(nums)
        keys = sorted(counter.keys())
        ans = []
        for i in range(len(keys)) :
            if i > 0 and keys[i] - keys[i - 1] == 1:
                print(keys[i])
                ans.append(counter[i] + counter[i - 1])
        print(ans)
        return max(ans)

A = Solution()
b = A.findLHS([1,3,2,2,5,2,3,7])
