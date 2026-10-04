class Solution:
    def hammingWeight(self, n: int) -> int:
        cmp = 1
        cnt = 0
        while n:
            if cmp & n == 1:
                cnt+=1
            n = n >> 1
        return cnt