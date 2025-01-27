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