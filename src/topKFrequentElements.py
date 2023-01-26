class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        ht = defaultdict(lambda: 1)
        for num in nums:
            ht[num] += 1
        ht = sorted(ht.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in ht[:k]]
