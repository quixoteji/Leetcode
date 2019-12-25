class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        return self.sol1(heightMap)

    # Solution 1 : brutal_force
    def sol1(self, heightMap):
        m, n = len(heightMap), len(heightMap[0])
        up = [[0 for _ in range(n)] for _ in range(m)]
        down = [[0 for _ in range(n)] for _ in range(m)]
        left = [[0 for _ in range(n)] for _ in range(m)]
        right = [[0 for _ in range(n)] for _ in range(m)]
        maxUp = [0 for _ in range(n)]
        maxDown = [0 for _ in range(n)]
        maxLeft = [0 for _ in range(m)]
        maxRight = [0 for _ in range(m)]
        for i in range(m) :
            for j in range(1) :
                maxUp[j] = up[i][j] = max(maxUp[j], heightMap[i][j])
                maxDown[j] = down[m-1-i][j] = max(maxDown[j], heightMap[m-1-i][j])
                maxLeft[i] = left[i][j] = max(maxLeft[i], heightMap[i][j])
                maxRight[i] = right[i][n-1-j] = max(maxRight[i], heightMap[i][n-1-j])
        ans = 0
        for i in range(m) :
            for j in range(n) :
                ans += 0 if heightMap[i][j] - min(up[i][j], down[i][j], left[i][j], right[i][j]) < 0 \
                    else heightMap[i][j] - min(up[i][j], down[i][j], left[i][j], right[i][j])
        return ans
                

A = Solution()
print(A.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1))


