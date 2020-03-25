#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = list()
        # queue.append(x)
        # queue.pop(0)
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
        
    def top(self) -> int:
        """
        Get the top element.
        """
        top = None
        for x in range(len(self.queue)) :
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

