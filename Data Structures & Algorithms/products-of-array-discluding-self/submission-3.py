class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        val = 1
        for i in range(1, len(nums)):
            val = val * nums[i-1]
            prefix[i] = val
        suffix = [1] * (len(nums))
        val = 1
        for i in range(len(nums)-2, -1,-1):
            val = val * nums[i+1]
            suffix[i] = val
        output = [1] * (len(nums))
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        return output