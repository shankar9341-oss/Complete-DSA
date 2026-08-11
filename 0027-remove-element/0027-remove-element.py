class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1
        return res