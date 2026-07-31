class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for n in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if j == n:
                    continue
                pdt *= nums[j]
            l.append(pdt)
        return l

        