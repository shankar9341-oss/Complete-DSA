class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            mid_squ = mid * mid
            if mid_squ == x:
                return mid
            elif mid_squ < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

