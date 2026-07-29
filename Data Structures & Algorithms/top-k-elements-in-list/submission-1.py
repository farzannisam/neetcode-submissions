class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = []
        for i in range(k):
            max = list(d.keys())[0]
            for j in d:
                if d[j] > d[max]:
                    max = j
            l.append(max)
            del d[max]
        return l

        