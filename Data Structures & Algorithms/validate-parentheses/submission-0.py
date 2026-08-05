class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "[":"]", "{":"}"}
        i = 0
        j = len(list(s)) - 1
        while i < j:
            if s[j] != d[s[i]]:
                return False
            i += 1
            j -= 1
        return True
        