class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        mapp = defaultdict(list)
        for r,char in reservedSeats:
            mapp[r - 1].append(char - 1)

        row = 0
        for k in mapp:
            row += 1
            v1 = all(not i in mapp[k] for i in range(1, 5))
            v2 = all(not i in mapp[k] for i in range(3, 7))
            v3 = all(not i in mapp[k] for i in range(5, 9))
            res += max(v2, v1 + v3)

        return res + (n - row) * 2