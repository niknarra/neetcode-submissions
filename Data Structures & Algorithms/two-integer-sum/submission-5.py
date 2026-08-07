class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()

        for idx, num in enumerate(nums):
            if (target - num) in diffs:
                return [diffs[(target - num)], idx]
            else:
                diffs[num] = idx
        
        return []
            