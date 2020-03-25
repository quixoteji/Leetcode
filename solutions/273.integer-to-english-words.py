#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def __init__(self) :
        self.num2str = {'0' : '', '1' : 'One', '2' : 'Two', '3' : 'Three',
            '4' : 'Four', '5' : 'Five', '6' : 'Six', '7' : 'Seven',
            '8' : 'Eight', '9' : 'Nine', '10' : 'Ten', '11' : 'Eleven',
            '12' : 'Twelve', '13' : 'Thirteen', '14' : 'Fourteen', '15' : 'Fifteen',
            '16' : 'Sixteen', '17' : 'Seventeen', '18' : 'Eighteen', '19' : 'Nineteen',
            '20' : 'Twenty', '30' : 'Thirty', '40' : 'Forty', '50' : 'Fifty',
            '60' : 'Sixty', '70' : 'Seventy', '80' : 'Eighty', '90' : 'Ninety'}
    
    def convert(self, n) :
        s = ''
        if n == 0 : return s
        if n >= 100 :
            s += self.num2str[str(n // 100)] + ' Hundred '
            n = n % 100
        if n >= 20 :
            ones = n % 10
            s += self.num2str[str(n - ones)] 
            if ones > 0 :
                s += ' ' + self.num2str[str(ones)]
        else :
            s += self.num2str[str(n)]
        return s

    def numberToWords(self, num: int) -> str:
        if num == 0 : return 'Zero'
        s = [' Billion', ' Million', ' Thousand', ''][::-1]
        nums = []
        while num > 0 :
            nums.append(self.convert(num % 1000).strip())
            num //= 1000
    
        ans = []
        for num, t in zip(nums, s) :
            if num : ans.append(num + t)
        # print(ans)
        return ' '.join(ans[::-1]).strip()
        
# @lc code=end

