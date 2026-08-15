class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 # Tracks the current unique value's index
        right = 1 # Tracks the current index

        while right < len(nums):
            # In case of unique value
            if nums[right] != nums[left]:
                # Swap with the next correct index and move both trackers
                nums[left+1], nums[right] = nums[right], nums[left+1]
                left += 1
                right += 1
            # In case of same values, move the right tracker to find the next unique value
            else:
                right += 1
        
        # Once right is out of bounds, left will be at the latest unique value's index
        # so left + 1 = count of unique values
        return left + 1