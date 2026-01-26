class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for x in range(amount+1)] for x in range(n+1)]

        for i in range(n+1): #num of ways to make the amount 0 with any number of coins
                dp[i][0] = 1 # 1 because i "choose no coins" as a way to get sum 0
        
        
        for i in range(1,n+1):
               for j in range(1,amount+1):
                       dp[i][j] = dp[i-1][j]   #ways to get amount j when we dont use ith coin
                       if j >= coins[i-1]:
                               dp[i][j] += dp[i][j-coins[i-1]]  #ways to get amount j when coin is used
        return dp[n][amount]

        