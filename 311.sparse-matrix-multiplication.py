#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start
class Solution:                
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return self.sol2(A, B)

    # Solution 1 : matrix multiplication
    def sol1(self, A, B) :
        ra, ca = len(A), len(A[0])
        rb, cb = len(B), len(B[0])
        C = [[0 for _ in range(cb)] for _ in range(ra)]

        for i in range(ra) :
            for j in range(cb) :
                a = A[i]
                b = [x[j] for x in B]
                for k in range(len(a)) :
                    C[i][j] += a[k] * b[k]
        return C

    # Solution 2 : hashmap
    def sol2(self, A, B) :
        def to_sparse(A) :
            sp = collections.defaultdict(dict)
            if not A : return sp
            for i in range(len(A)) :
                for j in range(len(A[0])) :
                    if A[i][j] != 0 : sp[i][j] = A[i][j]
            return sp
        
        def to_sparse_transpose(A) :
            sp = collections.defaultdict(dict)
            if not A : return sp
            for i in range(len(A)) :
                for j in range(len(A[0])) :
                    if A[i][j] != 0 : sp[j][i] = A[i][j]
            return sp

        def sparse2dense(sp, m, n) :
            res = [[0 for _ in range(n)] for _ in range(m)]
            for k, v in sp.items():
                for kk, vv in v.items():
                    res[k][kk] = vv
            return res

        spA = to_sparse(A)
        spB = to_sparse_transpose(B)
        spC = collections.defaultdict(dict)
        for i in spA.keys():
            for j in spB.keys():
                nonzero_idx = set(spA[i].keys()) & set(spB[j].keys())
                element = 0
                if nonzero_idx :
                    for idx in nonzero_idx :
                        element += spA[i][idx] * spB[j][idx] 
                    spC[i][j] = element
        return sparse2dense(spC, len(A), len(B[0]))


# @lc code=end

