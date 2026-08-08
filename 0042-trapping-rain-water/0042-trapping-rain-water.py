class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)
        waterStore = 0
        l_max = height[0]
        r_max = height[len(height)-1]

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max,height[left])
                waterStore += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max,height[right])
                waterStore += r_max - height[right]

        return waterStore