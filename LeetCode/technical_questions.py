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

# Find Pairs (Interview Question)           # Given two array of numbers, find pairs that equal to the target value
def find_pairs(arr1, arr2, target):
    arr2_set = set(arr2)                    # We convert arr2 to a set because checking if a number exists in a set is much faster than checking in a list.
    pairs = []                              # Create this to hold the pairs

    for num in arr1:                        #Loop through the first array
        complement = target - num           #Target minus a number to find if its in arr2_set
        if complement in arr2_set:          # Searching in a set (O(1) time)
            pairs.append((num, complement)) # Place the complement and num in pairs dict

    return pairs

# Find Kth node from the end (Interview Question)   # remove the node given to us starting at the end of the linked list *DO THIS WITHOUT USING LENGTH*
def find_kth_from_end(ll, k):
        slow = fast = ll.head                       # 11 is the linked list, and we are setting both pointers at the head of the linkedlist 
        for _ in range(k):                          # Loops through the linked list
            if fast is None:                        # If the fast pointer is pointing at a variable larger than K (target) return none
                return None
            fast = fast.next                        # Advances the fast pointer forward
 
        while fast:                                 # Moves the fast and slow pointer throughout the entire linkedlist until fast reaches the end
            slow = slow.next                        # EXPLAINATION: So we move the fast pointer to K (target), then move the slow pointer accordingly, until fast reaches nothing 
            fast = fast.next
        
        return slow

#  Longest Harmonious Subsequence (FREQUENCY COUNTER)   # Given an array, find where the difference is 1 among the harmonious sub-sequence 
def findLHS(self, nums: List[int]) -> int:
    count_dict = Counter(nums)                          # Store the numbers and count how many numbers are in the array 
    max_length = 0                                      # Keep track of how many harmonious subsequences there are 

    for num in count_dict:                              # Loop through the entire array 
        if num + 1 in count_dict:                       # Its going to check if the number after it exists (if 1 is the first number it will check if 2 is in the dict)
            current_length = count_dict[num] + count_dict[num + 1]    #If the above statement is true it will store it in current_length 
            max_length = max(max_length, current_length)              #This will store the current_length into max_length
        return max_length
    
# Maximum average subarray I                            # Given an array of numbers and a variable size K, find the maximum average of K 
def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_sum = sum(nums[:k])                             # Finds the sum of the first K elements
    window_sum = max_sum                                # Track current sum of window

    for i in in range(k, len(nums)):                    # Slide the window
        window_sum += nums[i] - nums[i - k]             # is going to move the window along (remove the first element and add a new element to the end)
        max_sum = max(max_sum, window_sum)              # Updates for the maximum sum found so far
    
    return max_sum/k                                    # Return the avg

# Deleting a node from a linked list                    # Given an singly linkedlist remove a node without having access to the head or the prev node and you cannot delete the last node
def deleteNode(self, node):
        node.val = node.next.val                        # Set the nodes value that you want to replace to the next nodes value
        node.next = node.next.next                      # you are going to skip over that node that you replace the value with

# How to reverse a linkedlist                           # Given a linkedlist reverse it so that the first node is the last and vice versa
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev  
            prev = curr  
            curr = next_node
        
        return prev

#Palindrome linked list 
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # Empty list or single node is always a palindrome
        
        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare both halves
        left, right = head, prev  # Start from the beginning and reversed second half
        while right:  # Compare until the end of the second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True 

# Merge two sorted lists                              # Given two linked list, merge them so that they are in numerical order 
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)                             # Creates a dummy node at the begining of the linkedlist
        tail = dummy                                    # sets tail to dummy

        while list1 and list2:                          # Traverse both lists
            if list1.val < list2.val:                   # If node in list 1 is less than node in list 2 
                tail.next = list1                       # Append list1 node
                list1 = list1.next                      # Move list1 pointer
            else:
                tail.next = list2                       # Append list2 node
                list2 = list2.next                      # Move list2 pointer
            
            tail = tail.next                            # Move tail pointer forward

        tail.next = list1 if list1 else list2           # If any elements remain in list1 or list2, append them

        return dummy.next                               # Return merged list (skip dummy node)

# Remove Nth Node from end of list 
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy   
        right = dummy 

        for _ in range (n+1):
            right = right.next
   
        while right: 
            left = left.next 
            right = right.next 

        if left.next:
            left.next = left.next.next

        return dummy.next

# Linked List Cycle 
def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False 

# First and Last position of element in sorted array 
def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)

# Find Minimum in Rotated Sorted Array
def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = left + (right - left) // 2
        
        # If mid element is greater than right element, search in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # Search in the left half
            
        return nums[left]

# Search in rotated sorted array 
def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:  
                if nums[left] <= target < nums[mid]:  
                    right = mid - 1
                else:  
                    left = mid + 1
            else:  
                if nums[mid] < target <= nums[right]:  
                    left = mid + 1
                else: 
                    right = mid - 1
        
        return -1

# Merge Sorted Array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1  # Initialize pointers

        # Merge from the end of nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:  # If nums1 element is larger
                nums1[p] = nums1[p1]
                p1 -= 1
            else:  # If nums2 element is larger
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1  # Move position to fill next largest value
        
        # If nums2 still has elements left, copy them into nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# Fizzbuzz 
def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

# Pascals Triangle 
def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]  # First row is always [1]
        
        for i in range(1, numRows):
            prev_row = pascal[-1]  # Get the previous row
            new_row = [1]  # First element is always 1
            
            # Compute middle elements
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])
            
            new_row.append(1)  # Last element is always 1
            pascal.append(new_row)  # Add new row to Pascal's Triangle
        
        return pascal