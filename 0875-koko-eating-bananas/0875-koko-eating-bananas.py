class Solution:
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            if self.eating(piles,mid,h):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

    def eating(self, piles,k , h):
        hrs = 0
        for p in piles:
            hrs += (p + k - 1) // k

        return hrs <= h
