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
