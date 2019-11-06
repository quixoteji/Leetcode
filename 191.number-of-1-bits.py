class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        for i in range(32) :
            k = k + 1 if n & (1 << i) else k
        return k