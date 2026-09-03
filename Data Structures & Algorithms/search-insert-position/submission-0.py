class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid + 1 < len(nums) and nums[mid+1] > target:
                    return mid+1
                i = mid+1
            else:
                if mid-1 >= 0 and nums[mid-1] < target:
                    return mid
                j = mid-1
        return i