class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            if (target - nums[n]) in nums:
                return [n, nums.index(target - nums[n])]
        