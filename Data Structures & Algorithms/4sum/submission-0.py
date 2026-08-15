class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for a in range(len(nums)-3):
            # Skip duplicate values for the first element 'a'
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            for b in range(a+1, len(nums)-2):
                # Skip duplicate values for the second element 'b'
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                left, right = b+1, len(nums) - 1

                while left < right:
                    if nums[a] + nums[b] + nums[left] + nums[right] == target:
                        res.append([nums[a], nums[b], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # Skip duplicate values for the third element 'c'
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        # Skip duplicate values for the fourth element 'd'
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif nums[a] + nums[b] + nums[left] + nums[right] > target:
                        right -= 1
                    
                    else:
                        left += 1
        
        return res
