#
# @lc app=leetcode id=353 lang=python3
#
# [353] Design Snake Game
#

# @lc code=start
from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.food = deque(food)
        self.width = width
        self.height = height
        self.bodyQueue = deque([(0, 0)])
        self.hashSet = set([(0, 0)])
        self.score = 0
        self.moveOps = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        s = self.hashSet
        q = self.bodyQueue
        ops = self.moveOps
        width = self.width
        height = self.height
        f = self.food
        
        if direction not in ops:
            return -1
        
        headi, headj = q[0]
        di, dj = ops[direction]
        headi, headj = headi + di, headj + dj
        if headi < 0 or headi >= height or headj < 0 or headj >= width:
            return -1
        
        q.appendleft((headi, headj))
        
        if f and [headi, headj] == f[0]:
            self.score += 1
            f.popleft()
        else:
            s.discard(q.pop())
            
        if (headi, headj) in s:
            return -1
        s.add((headi, headj))
        
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
# @lc code=end

