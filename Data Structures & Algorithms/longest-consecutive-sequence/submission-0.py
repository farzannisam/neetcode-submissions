class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in numset:
                c = 0
                while (n + c) in numset:
                    c += 1
                longest = max(c, longest)
        return longest