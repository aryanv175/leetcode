def fib(self, N: int) -> int:
        dp = [0 for x in range(N+1)]
        dp[0] = 0
        if N>=1:
            dp[1] = 1
            for x in range(2,N+1):
                dp[x] = dp[x-1]+dp[x-2]
        return dp[-1]
