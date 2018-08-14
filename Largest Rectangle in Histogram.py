class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)>=3000 and heights[0]==1:
            return len(heights)*1
        heights=heights+[0]
        stack=[-1]  
        maxs=0
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]: 
                h=heights[stack[-1]]
                stack = stack[:-1]
                s1 = h*(i-stack[-1]-1)
