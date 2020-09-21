#LettCode 53

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        newNum = maxTotal = nums[0]
        
        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i] + newNum) #This will give Maximum Ending Number so far
            maxTotal = max(newNum, maxTotal) #This will give Maximum Global Number so far
            
        return maxTotal
