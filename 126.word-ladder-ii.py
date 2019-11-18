#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return res
        # make the dictionary a set to speed up lookup
        words = set(wordList)
        # find candidate characters at each position
        chars = [set(w[i] for w in words) for i in range(len(beginWord))]
        
        # keep track of paths to each word from front and end, respectively
        front, back = defaultdict(list), defaultdict(list)
        # initially, we can only reach the begin word from the front, and the
        # end word from the end
        front[beginWord].append([beginWord])
        back[endWord].append([endWord])
        
        # flag to signal whether we are going forward from the front to end or 
        # backward. 
        forward = True
        
        # whenever there are paths for the next level
        while front:
            # create a map to keep track of the paths for the next level
            next_ = defaultdict(list)
            # try all the words and paths at the current level
            for w, paths in front.items():
                # create new words from the current ones
                for i in range(len(w)):
                    for c in chars[i]:
                        nw = w[:i] + c + w[i + 1:]
                        if nw not in words:
                            continue
                        # if the new word is found in the given dictionary, add 
                        # it to all the paths associated with its predecessor - 
                        # if we are going forward now, append the word to the 
                        # end of the paths at the current level; otherwise, 
                        # prepend the word to the front of the paths
                        next_[nw].extend([(p + [nw]) if forward else ([nw] + p) 
                                          for p in paths])
            # update current level with the new paths
            front = next_
            # check whether there are intersections between the paths from the 
            # front and those from the end. If so, it means they have met at 
            # specific words and thus can form a path from the beginning word to 
            # the end. Meanwhile, since the paths grow level-by-level with BFS, 
            # the end-to-end paths they form must be the shortest. 
            common = front.keys()&back.keys()
            if common:
                # if we are going backward now, swap the front and end 
                if not forward:
                    front, back = back, front
                # for every word shared between the front and end
                for w in common:
                    # concatenate the paths from the front and those from 
                    # the end
                    for f in front[w]:
                        for b in back[w]:
                            # since the word appears in both the paths, skip one
                            # occurrence to avoid duplicate
                            res.append(f + b[1:])
                # stop here since we have found all the shortest paths
                break
            
            # change the direction if one end has more paths than the other, 
            # which may slow down the search, and always prefer the end with 
            # fewer paths for potential speedup
            if len(front) > len(back):
                front, back, forward = back, front, not forward
            
            # remove used words from the dictionary to avoid cycles
            words -= front.keys()
        
        return res
        
# @lc code=end

