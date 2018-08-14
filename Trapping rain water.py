class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l=0  
        r=len(height)-1
        v=0
        mini=0
        while l<r:
            while(height[l]<=mini and l<r):  
                v += mini-height[l]
                l +=1
            while(height[r]<=mini and l<r): 
                v += mini-height[r]
                r -=1
            mini=min(height[l],height[r]) 
        return v
