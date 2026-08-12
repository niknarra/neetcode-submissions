class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        heap = []
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key in counts:
            heapq.heappush(heap, [counts[key], key])

            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res

