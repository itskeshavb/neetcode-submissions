class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        if digits == "":
            return []
        res = []
        def helper(i, subset):
            if i == len(digits):
                res.append(subset[:])
                return 
            for letter in mp[digits[i]]:
                helper(i+1, subset+letter)
        helper(0, "")
        return res