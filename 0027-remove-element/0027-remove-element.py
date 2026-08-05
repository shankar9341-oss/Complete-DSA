class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[result] = nums[i]
                result += 1
        return result