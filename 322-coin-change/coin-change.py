class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        #Below is a recursive solution

        # def f(i,amount):
            
        #     # base case
        #     if amount == 0:
        #         return 0
        #     if amount < 0 or (i==n and amount >0):
        #         return float('inf')
        #     skip = f(i+1,amount) #if i skip the coin
        #     take = 1+f(i,amount-coins[i]) #if i take the coin

        #     return min(skip,take)
        # ans = f(0,amount)
        # return -1 if ans == float('inf') else ans
        
        #Below is a tabulation: bottom up approach optimized

        # min coins(i) from 0 to n required to get the amount
        # dp[i][j] = min coins to make amount j using first i coins
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

        # amount 0 needs 0 coins (no matter how many coin types you have)
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                # skip current coin
                dp[i][j] = dp[i - 1][j]

                # take current coin (unbounded) if possible
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i - 1]])

        return -1 if dp[n][amount] == float('inf') else dp[n][amount]