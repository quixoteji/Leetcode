#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return self.sweepLine(buildings)

    # Solution 1 : divide and conquer
    def getSky(self, buildings) :
        n = len(buildings)
        # The base cases
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]] 
         
        # If there is more than one building, 
        # recursively divide the input into two subproblems.
        left_skyline = self.getSky(buildings[: n // 2])
        right_skyline = self.getSky(buildings[n // 2 :])
        
        # Merge the results of subproblem together.
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right) :
        '''
        Merge two skylines together
        '''
        def update_output(x, y) :
            '''
            Update the final output with the new element
            '''
            if not output or output[-1][0] != x :
                output.append([x, y])
            else : output[-1][1] = y
        
        def append_skyline(p, lst, n, y, curr_y) :
            '''
            Append the rest of the skyline elements with indice(p,n)
            '''
            while p < n: 
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y  = left_y = right_y = 0
        output = []
        # while we're in the region where both skylines are present
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick up the smallest x
            if point_l[0] < point_r[0]: 
                x, left_y = point_l
                p_l += 1
            else: 
                x, right_y = point_r 
                p_r += 1
            # max height (i.e. y) between both skylines
            max_y = max(left_y, right_y)
            # if there is a skyline change
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # there is only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # there is only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)
                
        return output

    # Solution 2 : sweep lines 
    def sweepLine(self, buildings) :
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        print(events)
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]
    
# @lc code=end

