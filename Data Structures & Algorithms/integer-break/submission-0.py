class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        maximize sum by breaking n into the sum of k positive integers

        n = 5

        3 2 --> 6

        max product 1 
        is 1
        max product 2
        is 1
        max product 3 
        is 2
        max product 4
        is 4
        max product 5 
        is 6

        max(mx_pod, i * dp[n-i])
        '''
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = 0 if i == n else i
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
        return dp[n]