class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Optimal Approach O(n) S and T

        # 1. Replace -ve values with 0s. -ves don't matter to us.
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # 2. Mark idx values of existing values as -ves
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        # 3. Find the first +ve value and return it's position
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1
