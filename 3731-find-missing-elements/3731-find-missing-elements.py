class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        min1 = nums[0]
        max1 = nums[-1]        
        ans = []
        for i in range(min1, max1):
            if i not in nums:
                ans.append(i)
        return ans