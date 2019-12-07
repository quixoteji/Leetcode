class Solution:
    def merge(self, intervals) :
        return self.sol1(intervals)

    # Solution 1 :
    def sol1(self, intervals) :
        intervals = sorted(intervals, key = lambda x : x[0])
        ans = []
        temp = intervals[0][:]
        for interval in intervals[1:] :
            if temp[1] >= interval[0] : 
                temp[1] = max(temp[1], interval[0])
            else : 
                ans.append(temp)
                temp = interval[:]
        ans.append(temp)
        return ans
                

A = Solution()
print(A.merge([[1,3],[2,6],[8,10],[15,18]]))


