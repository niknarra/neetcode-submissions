class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        currMax = float('-inf')
        ans = []
        currMaxIndex = -1
        heap = []

        while right < len(nums):
            # Add current element with its index
            heapq.heappush(heap, (-nums[right], right))
            
            # Once window reaches k
            if (right-left) + 1 == k:
                # Remove elements that are outside the window
                while heap[0][1] < left:
                    heapq.heappop(heap)
                
                # Heap top is now the max of the window
                ans.append(-heap[0][0])

                left += 1
            
            right += 1
        
        return ans