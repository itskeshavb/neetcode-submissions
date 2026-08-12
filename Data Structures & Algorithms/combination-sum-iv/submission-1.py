class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        '''
        for i in range(nums):
            if target - nums[i] = 0:
                dp[i] = dp[tar]

        recurrance relation is the the amount of ways to get to 1,2,3 plus what if we add any of the other nums. this is for the first example
        so for dp[4] we compute dp[0] + dp[1] + dp[2]
        '''
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(len(nums)):
                if i-nums[j]  >= 0:
                    dp[i]+=dp[i-nums[j]]
        return dp[target]