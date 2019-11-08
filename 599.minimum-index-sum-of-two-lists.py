#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        (list1, list2) = (list1, list2) if len(list1) < len(list2) else (list2, list1)
        hashtable1 = dict()
        hashtable2 = dict()
        for i, word in enumerate(list1) :
            hashtable1[word] = i
        for i, word in enumerate(list2) :
            hashtable2[word] = i

        ans = []
        for word in list1 :
            if word in hashtable2 : 
                ans.append([word, hashtable1[word] + hashtable2[word]])
        
        res = sorted(ans, key=lambda x : x[1])
        ans = []
        for word, val in res :
            if val == res[0][1] : ans.append(word)

        return ans 


        
# @lc code=end

