class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        mp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                mp=max(prices[r]-prices[l],mp)
            else:
                l=r
            r+=1
        return mp