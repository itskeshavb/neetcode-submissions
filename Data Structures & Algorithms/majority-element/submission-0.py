class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)
        res, resAmt = None, None
        for k,v in mp.items():
            if res == None:
                res = k
                resAmt = v
            elif v > resAmt:
                res = k
                resAmt = v
        return res
