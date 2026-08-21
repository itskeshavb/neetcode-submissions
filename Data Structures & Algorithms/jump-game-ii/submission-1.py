class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[n-1] = 0
        for i in range(n-2,-1,-1):
            for j in range(1, nums[i]+1):
                if i + j < n and dp[i + j] != -1:
                    if dp[i] == -1:
                        dp[i] = 1 + dp[i + j]
                    else:
                        dp[i] = min(dp[i], 1 + dp[i + j])
        return dp[0]
                