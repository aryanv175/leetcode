class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
    
    
    
    
"""class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < min(coins):
            return - 1
        if amount in coins:
            return 1

        prev = coins.copy()
        res = float('inf')
        num  = 0
        temp = amount
        while prev:
            while amount > 0 and coins:
                if amount >= max(coins) and (amount - max(coins) >= min(coins) or amount - max(coins) == 0):
                    print(amount)
                    amount -= max(coins)
                    num += 1
                else:
                    coins.remove(max(coins))
            if amount == 0:
                res = min(num, res)
            num = 0
            amount = temp
            if len(prev) > 0:
                prev.remove(max(prev))
            coins = prev.copy()
        print(res)
        if res != float('inf'):
            return res
        return -1"""
