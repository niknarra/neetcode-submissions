class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] != nums[left]:
                nums[left+1], nums[right] = nums[right], nums[left+1]
                left += 1
                right += 1
            else:
                right += 1
        
        return left + 1