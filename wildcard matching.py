class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i,j,star,point=0,0,-1,0
        while i<len(s):
            if j<len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j<len(p) and p[j] == '*':
                star = j
                j += 1
                point = i  
            elif star!=-1:  
                j = star + 1  
                point +=1
                i = point
            else:
                return False
        while j<len(p) and p[j] == '*':  
            j += 1
        if j != len(p): return False
        return True
