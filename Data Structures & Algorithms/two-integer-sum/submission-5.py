class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = collections.defaultdict(int)
        for n in range(len(nums)):
            num = nums[n]
            diff = target - num
            if diff in d:
                return [d[diff], n]
            d[num] = n
        return []
        