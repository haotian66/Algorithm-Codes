class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        stack,m = [],0
        for i in range(len(s)):
            if stack and s[i] == ')' and s[stack[-1]]=='(':  
                stack = stack[:-1]
            else:
                stack += [i]
        if not stack: return len(s)
        if len(stack)>1:
            for i in range(1,len(stack)): 
                m = max(stack[i] - stack[i-1]-1, m)
        return max(m,stack[0],len(s)-stack[-1]-1) 
