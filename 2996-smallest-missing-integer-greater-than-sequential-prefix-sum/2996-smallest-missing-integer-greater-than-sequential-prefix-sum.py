class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        seq = nums[0]
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1] + 1:
                seq += nums[j]
            else:
                break
        sett = set(nums)
        while seq in sett:
            seq += 1
        return seq
