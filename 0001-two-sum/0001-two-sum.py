class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            sum1 = target - n
            if sum1 in hashmap:
                return [hashmap[sum1], i]
            hashmap[n] = i
        
                
        
                
        
