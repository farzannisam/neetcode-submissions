class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        pref, post = 1, 1
        for i in range(len(nums)):
            l[i] = pref
            pref *= nums[i]
        print(l)
        for i in range(len(nums) - 1, -1, -1):
            l[i] *= post
            post *= nums[i]
        return l

        