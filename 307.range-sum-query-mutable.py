#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class NumArray:
    # Solution 1 : time limit exceeded
    # def __init__(self, nums: List[int]):
    #     self._nums = nums[:]
    #     self._dp = [ 0 for _ in range(len(nums) + 1)]
    #     for x in range(1, len(self._dp)) :
    #         self._dp[x] = sum(nums[0:x])
        

    # def update(self, i: int, val: int) -> None:
    #     for x in range(i + 1, len(self._dp)) :
    #         self._dp[x] += val - self._nums[i]
    #     self._nums[i] = val

    # def sumRange(self, i: int, j: int) -> int:
    #     return self._dp[j + 1] - self._dp[i]

    # Solution 2 : Segment Tree
    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, i: int, val: int) -> None:
        self.st.update(i,val)

    def sumRange(self, i: int, j: int) -> int:
        return self.st.get_sum_in_range(i,j)    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

class Node :
    def __init__(self, input, start, end) :
        self.rangeStart = start
        self.rangeEnd = end
        self.left = None
        self.right = None
        if start == end : self.sum = input[start]
        else :
            middle = start + ((end - start) // 2)
            self.left = Node(input, start, middle)
            self.right = Node(input, middle + 1, end)
            self.sum = self.left.sum + self.right.sum

    def is_in_range(self, index) :
        return self.rangeStart <= index <= self.rangeEnd

class SegmentTree :
    def __init__(self, input) :
        self.input = input
        self.rootNode = Node(input, 0, len(input) - 1) if input else None

    def update(self, index, value) :
        node = self.rootNode
        diff = value - self.input[index]
        while node :
            node.sum += diff
            if node.left and node.left.is_in_range(index) : node = node.left
            else : node = node.right
        self.input[index] = value

    def get_sum_in_range(self, start, end) :
        return self.get_sum(self.rootNode, start, end)

    def get_sum(self, node, start, end) :
        if node.rangeStart == start and node.rangeEnd == end : 
            return node.sum
        else :
            sumV = 0
            if node.left and node.left.is_in_range(start):
                sumV += self.get_sum(
                    node.left, start, node.left.rangeEnd if end > node.left.rangeEnd else end)
            if node.right and node.right.is_in_range(end):
                sumV += self.get_sum(
                    node.right, node.right.rangeStart if start < node.right.rangeStart else start, end)
            return sumV
            
# @lc code=end

