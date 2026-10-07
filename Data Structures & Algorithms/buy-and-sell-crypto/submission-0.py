class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # buy day, sell day
        maxP = 0 # [10,2,5,6,10,1,3]

        while r < len(prices):
            if prices[r] > prices[l]: # we can make a profit!
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                r +=1 # we keep looking for higher prices.
                continue
            else:
                l = r # our buying day updates to the smallest price
                r += 1
                continue
        return maxP