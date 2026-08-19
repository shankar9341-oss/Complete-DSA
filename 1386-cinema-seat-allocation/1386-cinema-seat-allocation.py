class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        mapp = defaultdict(set)
        for r,c in reservedSeats:
            mapp[r - 1].add(c - 1)

        for row in mapp.values():
        
            left = all(i not in row for i in range(1, 5))
            mid = all(i not in row for i in range(3, 7))
            right = all(i not in row for i in range(5, 9))
            if left and right:
                res += 2
            elif left or mid or right:
                res += 1
        return res + (n - len(mapp)) * 2