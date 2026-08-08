class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first(nums,target):
            left = 0
            right = len(nums)-1
            result = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        def last(nums,target):
            left = 0
            right = len(nums)-1
            result = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        return [first(nums,target),last(nums,target)]

        
