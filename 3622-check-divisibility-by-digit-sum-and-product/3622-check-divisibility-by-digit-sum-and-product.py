class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        total_sum = 0
        total_prod = 1
        while temp:
            total = temp % 10
            total_sum += total
            total_prod *= total
            temp //= 10
        return n % (total_sum + total_prod) == 0
        