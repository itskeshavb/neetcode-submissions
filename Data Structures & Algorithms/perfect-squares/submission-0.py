class Solution:
    def numSquares(self, n: int) -> int:
        '''
        23 --> 16 4 1 1 1
        23 --> 9 9 4 1
        not greedy
        similar to coin change where we have our set coins til n
        and we run a double for and we find the least number for values 1 to n
        for i in range len(values):
            for j in range n:


        '''
        dp = [n] * (n+1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1, target+1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])
        return dp[n]
                
