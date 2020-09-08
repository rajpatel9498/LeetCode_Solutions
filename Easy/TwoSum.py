# Solution - 1 Using Dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictonary = {}
        
        for i in range(len(nums)):
            
            x = target - nums[i]
            
            if x in dictonary.keys():
                return (dictonary[x],i)
            else:
                dictonary[nums[i]] = i
                
# Solution - 2 Using For loop

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if (nums[j] + nums[i]) == target:
                    return i,j
