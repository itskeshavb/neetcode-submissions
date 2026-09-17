class Solution:
    def mySqrt(self, x: int) -> int:
        if x== 0:
            return 0
        minVal = 1
        l,r = 1, x
        while l <= r:
            mid = (l+r) // 2
            if mid * mid == x:
                return mid
            elif mid*mid < x:
                minVal = max(minVal, mid)
                l = mid + 1
            else:
                r = mid -1 
        return minVal
