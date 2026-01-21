class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0]*len(prices)
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
                else:
                    answer[i] = prices[i]
            if i == (len(prices)-1):
                answer[i] = prices[i]
        return answer
