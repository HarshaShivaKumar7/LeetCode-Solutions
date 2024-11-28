import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        min_heap = []
        for element, freq in counts.items():
            heappush(min_heap, (freq, element))
            if len(min_heap) > k:
                heappop(min_heap)
        return [num for (count, num) in min_heap]

        # k=2

        # 1-3
        # 2-2
        # 3-1
