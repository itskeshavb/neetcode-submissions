class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        we either choose to buy or not
        if we choose to buy then we want to sell where it will max
        the rest

        dp[i] = where we sell so from prices[j]-prices[i] + dp[j+1]
        
        '''
        dp = [0] * (len(prices)+1)
        for i in range(len(prices)-2,-1,-1):
            dp[i] = dp[i+1]
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > 0:
                    dp[i] = max(dp[i], prices[j]-prices[i]+ dp[j+1])
        return max(dp)