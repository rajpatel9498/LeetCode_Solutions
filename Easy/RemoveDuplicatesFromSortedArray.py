class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        dict = {}
        j=0
        for i in range(len(nums)):
            
            
            
            if nums[i] in dict.keys():
                continue
            else:
                dict[nums[i]] = j
                j=j+1
        list = [] 
        for key in dict.keys(): 
            list.append(key) 
        l = len(list)
        print(l)
        return list
