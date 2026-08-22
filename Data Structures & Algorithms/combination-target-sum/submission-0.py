class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        self.helper(res, nums, subset, 0, target)
        return res

    def helper(self, res,nums, subset, i, target):
        if target < 0 or i >= len(nums):
            return
        if target == 0:
            res.append(subset[:])
            return
        subset.append(nums[i])
        self.helper(res, nums, subset, i, target-nums[i])
        subset.remove(nums[i])
        self.helper(res, nums, subset, i+1, target)
        return