class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        heap = []
        res = []

        for num in arr:
            heapq.heappush(heap, [-abs(x-num), -num] )

            if len(heap) > k:
                heapq.heappop(heap)
            
        
        while heap:
            res.append(-heapq.heappop(heap)[1])
        
        return sorted(res)