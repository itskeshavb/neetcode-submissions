class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n)
        dp[n-1] = True
        for i in range(n-2, -1,-1):
            for j in range(nums[i]+1):
                if i+j < n and dp[i+j]:
                    dp[i] = True
        return dp[0]
                    

