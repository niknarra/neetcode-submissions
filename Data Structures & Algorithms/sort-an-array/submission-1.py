class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 1. Approach 2 -> Merge Sort

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
        
            return merge(left, right)
        
        def merge(left, right):
            i = 0
            j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                elif left[i] > right[j]:
                    res.append(right[j])
                    j += 1
                else:
                    res.extend([left[i], right[j]])
                    j += 1
                    i += 1
            
            while i < len(left):
                res.append(left[i])
                i += 1
            
            while j < len(right):
                res.append(right[j])
                j += 1

            return res

        return merge_sort(nums)