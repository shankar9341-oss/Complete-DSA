class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                sett.remove(nums[left])
                left += 1
            if nums[right] in sett:
                return True
            sett.add(nums[right])
        return False
        