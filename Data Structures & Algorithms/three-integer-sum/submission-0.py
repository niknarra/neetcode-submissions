class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for a in range(len(nums) - 2):
            # Skip duplicate values for the first element 'a'
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            left, right = a + 1, len(nums) - 1

            # Must be strictly less than (<) to ensure two unique elements
            while left < right:
                current_sum = nums[a] + nums[left] + nums[right]

                if current_sum == 0:
                    # Append the elements together as a single triplet list
                    res.append([nums[a], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second element 'left'
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicate values for the third element 'right'
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
