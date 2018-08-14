class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        if not intervals:
            return [newInterval]
        s,b= newInterval.start, newInterval.end  
        left=right=[]  
        for i in range(len(intervals)):
            if intervals[i].end>=newInterval.start:
                break
            left=left+[intervals[i]]
        for i in range(len(intervals)-1,-1,-1):
            if intervals[i].start<=newInterval.end:
                break
            right=[intervals[i]]+right  

        if left+right!=intervals: 
            s=min(newInterval.start,intervals[len(left)].start) 
            b=max(newInterval.end, intervals[len(intervals)-len(right)-1].end)
        return left+[Interval(s,b)]+right  
