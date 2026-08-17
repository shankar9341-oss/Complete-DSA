class Solution:
    def fib(self, n: int) -> int:
        # if (n == 0 or n == 1):
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)      

        ans = [0,1]
        for i in range(2, n + 1):
            ans.append(ans[i - 1] + ans[i - 2])
        return ans[n]  