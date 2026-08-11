class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 1. Approach 1 -> Heap Sort
        # Build a min heap and pop elements
        # Each pop is log(n), n elements -> n log(n) satisfying the ask
        heap = [] 
        res = []

        for num in nums:
            heapq.heappush(heap, num)

        while heap:
            res.append(heapq.heappop(heap))

        return res