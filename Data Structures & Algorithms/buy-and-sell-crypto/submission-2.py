class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r <= len(prices) -1:
            curr = prices[r] - prices[l]
            if prices[r] > prices[l]:
                r +=1
                if curr > profit:
                    profit = curr
            else: 
                l = r
                r += 1

        return profit
           
            