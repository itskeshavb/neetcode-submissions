class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        keep track of prev ineq
        for the first value
        keep sliding the right pointer until it fails and then when 
        it fails then we slide the left pointer
        bounds would be while the right point is less than len(arr)
        and while l < r and l < len(arr)
        '''
        if not arr:
            return 0
        res = 1
        prev = ""
        l = 0
        r = 1
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1)
                r+=1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l+1)
                r+=1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""
        return res

