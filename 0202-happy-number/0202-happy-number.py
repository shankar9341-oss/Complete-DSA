class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        res = str(n)
        while res not in sett:
            sett.add(res)
            sum1 = 0
            for digit in res:
                digit = int(digit)
                sum1 += digit ** 2
            if sum1 == 1:
                return True
            res = str(sum1)
        return False