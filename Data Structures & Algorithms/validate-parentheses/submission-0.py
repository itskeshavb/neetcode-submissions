class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")" : "(", "]" : "[", "}" : "{" }
        for srs in s:
            if srs in mp:
                if stack and stack[-1] == mp[srs]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(srs)
        return True if not stack else False