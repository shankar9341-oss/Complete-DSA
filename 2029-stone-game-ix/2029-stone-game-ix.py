class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        idx0 = 0
        idx1 = 0
        idx2 = 0
        for stone in stones:
            rem = stone % 3
            if rem == 0:
                idx0 += 1
            elif rem == 1:
                idx1 += 1
            else:
                idx2 += 1
        if idx0 % 2 == 0: return idx1 > 0 and idx2 > 0
        return abs(idx1 - idx2) > 2