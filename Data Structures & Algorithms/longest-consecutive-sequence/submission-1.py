class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0
        s = set(nums)
        for i in nums:
            if (i - 1) not in s:
                count = 0
                while (count + i) in s:
                    count += 1
                maxcount = max(count, maxcount)
        return maxcount