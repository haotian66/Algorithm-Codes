class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import *
        if not s or not words: return []
        lensingle = len(words[0])
        lenall = lensingle * len(words)
        worddict = Counter(words)
        out = []
        for i in range(lensingle):
            left = right = i
            currdict = {}
            while right + lensingle <= len(s):  
                word = s[right:right+lensingle] 
                right += lensingle
                if word in worddict:
                    if word in currdict: currdict[word] += 1
                    else: currdict[word] = 1
                    while currdict[word] > worddict[word]:
                        currdict[s[left:left + lensingle]] -= 1 
                        left += lensingle
                    if len(s[left:right]) == lenall: out.append(left)
                else: 
                    currdict = {}
                    left = right
        return out
