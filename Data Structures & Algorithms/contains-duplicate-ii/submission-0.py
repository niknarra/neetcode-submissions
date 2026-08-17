class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tracker = {}

        for idx, num in enumerate(nums):
            if num in tracker:
                if abs(tracker[num] - idx) <= k:
                    return True
            
            tracker[num] = idx
        
        return False