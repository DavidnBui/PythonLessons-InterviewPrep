# Popular interview Technical Questions

# Two Sum 
# Given an array of integers detertime what two numbers add up to the target 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []

# How to reverse a linked list (Assume you created the node and linkedlist class)
    def reverse (self):                 # VERY COMMON INTERVIEW QUESTION
        temp = self.head                # Line 111 --> Line 113 Reverses the head and tail
        self.head = self.tail 
        self.tail = temp
        after = temp.next              
        before = None
        for _ in range(self.length):
            after = temp.next           # Moves after varaible over one 
            temp.next = before          # Makes temp variable flip and point to the item before
            before = temp               # Moves before variable over one
            temp = after                # Moves temp variable behind one

# Has Loop 
# Determines if your linked list is a loop 
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# When given two lists, 
# determine if the two lists have a common variable
    def item_in_common(list1,list2):
        my_dict = {}
        for i in list1:
            my_dict[i] = True
        
        for j in list2:
            if j in my_dict:
                return True
        
        return False

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

# ITEM IN COMMON (INTERVIEW QUESTION) # Given two lists of numbers find the number that is in both
def item_in_common(list1, list2):   # REMEMBER TO DEFINE THE FUNCTIOn
    count = {}                      # Creates a dictionary to hold the values 
    
    for num in list1:               # Loop through the values of list1
        count[num] = True           # Store Numbers of List1 into dictionary 
    
    for num in list2:               # Loop through the values of list2
        if num in count:            # If numbers in list 2 are in list 1 return true 
            return True 
            
    return False

# FIND DUPLICATES (INTERVIEW QUESTION)  # Given an array of numbers find the numbers that have duplicates in it 
def find_duplicates(nums):          
    count = {}                      # Going to hold the values of the array
    duplicates = []                 # Going to hold duplicates value once we loop through the entire thing

    for num in nums:                # Iterating through the literal list 
        if num in count:
            count[num] += 1         # Add 1 to the value if we have seen it already in count
        else:
            count[num] = 1          # Make value equal to 1 because it is the first instance we see it

    for num, freq in count.items(): # Collect numbers that appear more than once
        if freq > 1:
            duplicates.append(num)

    return duplicates

#First Non-Repeating Characters (INTERVIEW QUESTION)   # given a string, return the first letter that does not repeat
def first_non_repeating_char(string):
    dict = {}                                   # hold the information given to us 
    
    for char in string:                         # loop through the string that is given to us and stores in "dict"
        dict[char] = dict.get(char, 0) + 1      # Checks if the character is in dict, if not assign it a value of 1. If it is increment it 
        
    for char in string:                         #Loops through the string again 
        if dict[char] == 1:                     # Finds the first character that holds the value of 1 
            return char
            
    return None


#Group Anagrams (INTERVIEW QUESTION)        # Given a series of strings, group them if they make an anagram of each other
def group_anagrams(strings):
    count_dict = {}

    for word in strings:                      # Iterate through each word in the list
        sorted_word = "".join(sorted(word))  # Sort characters alphabetically

        if sorted_word not in count_dict:
            count_dict[sorted_word] = []  # Initialize list if key is not present

        count_dict[sorted_word].append(word)  # Append word to correct anagram group

    return list(count_dict.values())  # Return grouped anagrams as lists

# Subarray_sum (INTERVIEW QUESTION)     # Given an array of numbers find a contiguous sequence that adds up to the target
def subarray_sum(nums, target):         #SLIDING WINDOW APPROACH
    left = 0                            # Create a pointer at the index of 0
    current_sum = 0                     # Keeps track of the current sum of the window

    for right in range(len(nums)):      # Moves the right pointer through the array
        current_sum += nums[right]      # Adds the element to the window 
    
        while current_sum > target and left <= right:   # Our condition 
            current_sum -= nums[left]                   # Remove leftmost value
            left += 1                                   # Move left pointer forward

        if current_sum == target:       # If sum equals target, return indices
            return [left, right]

    return []

# Remove Duplicates (INTERVIEW QUESTION)    #Initial though was to use frequency counter 
def remove_duplicates(my_list):             #It works but it is not time effecient 
    return list(set(my_list))               #Instead use a set because it automactically gets rid of duplicates

# Has Unique Chars (Interview Question)
def has_unique_chars(string):
    return len(set(string)) == len(string)  # set(string), converts the string into a set. Which then gets rid of the duplicates automatically 
                                            # It then compares the set to the length of the string, If it is the same length then it returns true(they were all unique) & vice versa