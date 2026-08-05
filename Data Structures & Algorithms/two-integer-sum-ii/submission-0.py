class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for n in range(len(numbers)):
            diff = target - numbers[n]
            if diff in d:
                return [d[diff] + 1, n+1]
            d[numbers[n]] = n
        return []
        