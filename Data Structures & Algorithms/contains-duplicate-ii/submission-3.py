class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding Window approach
        # Maintain a window of size k
        # If an element appears twice in the current window,
        # it satisfies abs(i - j) <= k
    
        right = 0
        seen = set()

        while right < len(nums):
            if nums[right] in seen:
                return True
            
            seen.add(nums[right])
            
            if len(seen) > k:
                seen.remove(nums[right-k])

            right += 1
        
        return False
            

