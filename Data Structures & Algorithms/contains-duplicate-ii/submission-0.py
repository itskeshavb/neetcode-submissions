class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        l = 0
        arr = set()
        for r in range(len(nums)):
            if abs(r-l) > k:
                arr.remove(nums[l])
                l+=1
            if nums[r] in arr:
                return True
            arr.add(nums[r])
        return False

            

        