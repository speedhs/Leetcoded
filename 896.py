class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if (nums[0]<nums[1]):
            for i in range(1,len(nums)-1):
                for j in range (i+1,len(nums)):
                    if(nums[i]>nums[j]):
                        return False
        elif (nums[0]>nums[1]):
            for i in range(1,len(nums)-1):    
                for j in range (i+1,len(nums)):
                    if(nums[i]<nums[j]):
                        return False
        return True