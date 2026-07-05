class Solution:
    def helper(self, coins: List[int], amount: int) -> int:  
        if amount in self.memo:
            return self.memo[amount]
        min_count = float('inf') #min(x, y, z)
        for coin in coins:
            if coin <= amount:
                coins_needed = self.helper(coins, amount-coin)
                min_count = min(min_count, coins_needed)
        if min_count != float('inf'):
            min_count +=1
        self.memo[amount] = min_count
        return min_count
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        #min num of coins needed to make the remaining amount
        # amount = min(x, y, z) + 1
        self.memo = {}
        self.memo[0] = 0
        for coin in coins:
            if coin <= amount:
                self.memo[coin] = 1
        coins.sort()
        value = self.helper(coins, amount)
        return value if value != float('inf') else -1