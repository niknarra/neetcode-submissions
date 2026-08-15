class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr = 0

        while curr < len(nums):
            currNum = abs(nums[curr])

            if nums[currNum - 1] < 0:
                return currNum
            else:
                nums[currNum - 1] *= -1
            
            curr += 1
        
        return -1