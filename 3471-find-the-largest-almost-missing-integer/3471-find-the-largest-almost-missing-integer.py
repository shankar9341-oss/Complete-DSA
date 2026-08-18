class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        mapp = defaultdict(int)
        for num in nums:
            mapp[num] += 1

        unq = [num for num, val in mapp.items() if val == 1]
        
        if k == 1:
            return max(unq) if unq else -1
        first = nums[0] if mapp[nums[0]] == 1 else -1
        last = nums[-1] if mapp[nums[-1]] == 1 else -1
    
        return max(first,last)