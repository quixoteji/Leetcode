#
# @lc app=leetcode id=379 lang=python3
#
# [379] Design Phone Directory
#

# @lc code=start
class node :
    def __init__(self, val) :
        self.val = val
        self.next = None

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.head = ListNode(0)
        dummy = self.head
        for i in range(1, maxNumbers) : 
            dummy.next = ListNode(i)
            dummy = dummy.next

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.head :
            val, self.head = self.head.val, self.head.next
        else :
            val = -1
        return val

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        dummy = self.head
        while dummy :
            if dummy.val == number : return True
            dummy = dummy.next
        return False

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if self.check(number) : return
        if self.head :
            dummy = self.head
            while dummy.next : dummy = dummy.next
            dummy.next = ListNode(number)
        else :
            self.head = ListNode(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
# @lc code=end

