
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x):
            total = 0
            n = len(coins)
            for i in range(1, n + 1):
                for comb in combinations(coins, i):
                    lcm = comb[0]
                    for c in comb[1:]:
                        lcm = lcm * c // gcd(lcm, c)
                    if i % 2:
                        total += x // lcm
                    else:
                        total -= x // lcm
            return total

        left = 1
        right = 10 ** 18
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left