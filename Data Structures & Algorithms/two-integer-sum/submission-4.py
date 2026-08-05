class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            if (target - nums[n]) in nums:
                temp = nums[n]
                nums[n] = 0
                return [n, nums.index(target - temp)]
        