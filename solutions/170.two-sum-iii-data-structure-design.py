#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#

# @lc code=start
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nums = list() 
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self._nums.append(number)



    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        hashset = set()
        for num in self._nums :
            if num in hashset : return True
            else : hashset.add(value - num)
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

