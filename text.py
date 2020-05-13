# countries = ['USA', 'CAN', 'MEX']
# pops = [330, 30, 100]

# class Sampler :
#     def __init__(self, countries, pops) :
#         self.countries = countries
#         self.pops = pops
#         self.presum = [0 for _ in range(len(self.pops) + 1)]
#         for i in range(1, len(pops) + 1) :
#             self.presum[i] = self.presum[i-1] + self.pops[i-1]

#     def sampler(self, num = None) :
#         l, r = 0, len(self.presum)
#         while l <= r :
#             mid = l + (r - l) // 2
#             if self.presum[mid] < 

# class Solution:
#     def longestIncreasingPath(self, matrix) :
#         if not matrix : return 0
#         m, n = len(matrix), len(matrix[0])
#         mem = [[0 for _ in range(n)] for _ in range(m)]
#         ans = 0
#         for i in range(m) :
#             for j in range(n) :
#                 ans = max(ans, self.dfs(mem, matrix, i, j))
#         return ans
    
    
#     def dfs(self, mem, matrix, i, j) :
#         if mem[i][j] != 0 : return mem[i][j]
#         m, n = len(matrix), len(matrix[0])
#         dirs = [1, 0, -1, 0, 1]
#         for d in range(4) :
#             x, y = i + dirs[d], j + dirs[d + 1]
#             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] :
#                 mem[i][j] = max(mem[i][j], self.dfs(mem, matrix, x, y))
#         mem[i][j] += 1
#         return mem[i][j]

# s = Solution()
# matrix = [[9,9,4],[6,6,8],[2,1,1]]
# print(s.longestIncreasingPath(matrix))

A = [1, 0, 0, 0, 2, 0, 0, 3, 4, 0, 0, 0]
B = [5, 0, 0, 0, 6, 7, 0, 0, 4, 0, 1, 0]
import collections
def product(A, B) :
    hashmapA = collections.defaultdict(int)
    hashmapB = collections.defaultdict(int)
    for i, num in enumerate(A) :
        hashmapA[i] = num
    for i, num in enumerate(B) :
        hashmapB[i] = num
    
    ans = 0
    for key in hashmapA :
        if key in hashmapB :
            ans += hashmapA[key] * hashmapB[key]
    return ans

print(product(A, B))
