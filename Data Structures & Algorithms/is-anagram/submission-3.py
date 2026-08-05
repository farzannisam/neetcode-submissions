class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = sorted(s)
        m = sorted(t)
        if len(n) != len(m):
            return False
        return n == m
        