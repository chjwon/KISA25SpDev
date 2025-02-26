class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price: 
                min_price = prices[i]

            if (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price
            else:
                pass

        return max_profit