class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp = list(nums)
        nums.sort()
        if(nums[len(nums)-1] >= nums[len(nums)-2]*2):
            for i in range (len(nums)):
                if (temp[i] == nums[len(nums)-1]):
                    return i
        return -1
        