# Problem Solving Patterns 

#Frequency Counter

# Two - Sum 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], i]
        dictionary[num] = i

# Two Pointers

# Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else: 
                nums[left] != val
                left += 1
        return left

