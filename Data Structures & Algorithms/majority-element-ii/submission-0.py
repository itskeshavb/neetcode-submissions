import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        have a counter dict 
        then for each number we see if the amount is greater than
        math.floor(n/3) and if so thenw e add to the result
        '''
        mp = Counter(nums)
        res = []
        n = len(nums)
        check = math.floor(n/3)
        for k,v in mp.items():
            if v > check:
                res.append(k)
        return res