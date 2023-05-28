# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # this is the function we will use to reverse the other half of the list
        # which we can later compare with the first half using the fast node.

        def reverse(head: ListNode) -> ListNode:
            prev  = None              #  head
            while head:                 # 1  -> 2  ->  3
                nex = head.next         #       nex
                head.next = prev      # prev = None <- 1     2 -> 3
                prev = head            #               prev  nex
                head = nex             #        None <- 1    2(head) -> 3    
            return prev
                

        # we have to halve the linkedlist to do that, we can use a slow pointer and a fast pointer that will move 
        # at twice the speed of the slow pointer.

        fast = slow = head
        while fast and fast.next:# we use this loop to find the mid point of the linkedlist
            fast = fast.next.next 
            slow = slow.next
        
        fast = head
        slow = reverse(slow) # called the function to reverse the linkedlist

        while slow: 
            if slow.val != fast.val: # if the values of slow and fast are not equal, it it not a palindrome
                return False
            
            fast = fast.next
            slow = slow.next

        return True # otherwise return True!
