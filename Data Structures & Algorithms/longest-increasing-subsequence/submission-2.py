class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp[i] = length of lis at that point
        dp[i] = max(dp[i], dp[j] + 1)
        where j < i and nums[i] > nums[j]
        '''
        n = len(nums)
        dp = [1] * (n)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
