class Solution(object):
    def maxProfit(self, prices):
        answer = [0]
        min_prices = prices[0]
        
        for i in range(1,len(prices)):
            if min_prices > prices[i]:
                min_prices = prices[i]
            answer.append(max(answer[i-1],prices[i]-min_prices))
        return answer[-1]