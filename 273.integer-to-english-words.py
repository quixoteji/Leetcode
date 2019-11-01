#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def __init__(self) :
        dict_1 = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six', 
                7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten', 11 : 'Eleven', 12 : 'Twelve',
                13 : 'Thirteen', 14 : 'Fourteen', 15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen',
                18 : 'Eighteen', 19 : 'Nineteen', 0 : 'Zero'}
        dict_2 = {2 : 'Twenty', 3 : 'Thirty', 4 : 'Fourty', 5 : 'Fifty', 6 : 'Sixty', 
                7 : 'Seventy', 8 : 'Eighty', 9 : 'Ninety'}
        
            
    def numberToWords(self, num: int) -> str:
        if num == 0 : return 'Zero'
        ans = []
        s = str(num)[::-1]

        
# @lc code=end

