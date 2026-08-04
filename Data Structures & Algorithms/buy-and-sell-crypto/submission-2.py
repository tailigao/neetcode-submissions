class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = [prices[0]]
        profit = []
        for i in range(len(prices)-1):
            sell = prices[i+1]
            profit.append(sell - min(seen))
            seen.append(sell)


        if len(profit) > 0 and max(profit) > 0:
                return max(profit)
        else: 
            return 0


            


        