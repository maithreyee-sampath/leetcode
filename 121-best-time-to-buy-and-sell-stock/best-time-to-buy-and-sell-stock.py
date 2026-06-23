class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = float('-inf')

        while right<len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right += 1
            
        return max(profit, 0)