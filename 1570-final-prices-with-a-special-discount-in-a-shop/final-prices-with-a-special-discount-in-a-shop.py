class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                curr = stack.pop()
                answer[curr] = prices[curr] - prices[i]
            stack.append(i)

        return answer


