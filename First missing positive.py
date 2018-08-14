class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        i=0
        while(i<l):
            if (nums[i]>0 and nums[i]!=i+1 and nums[i]<=l):  
                if nums[i]==nums[nums[i]-1]:  
                    nums[i]=-1
                    continue
                t=nums[nums[i]-1]  
                nums[nums[i]-1]=nums[i]
                nums[i]=t
            else:
                i+=1
        for i in range(l):
            if nums[i]!=i+1:
                return i+1
        return l+1  
