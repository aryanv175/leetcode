# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        def reverse(head: ListNode) -> ListNode: # function used to reverse the linkedlist at the mid point
            prev = None

            while head:
                nex = head.next
                head.next = prev
                prev = head
                head = nex
            
            return prev
        # pretty  simple two pointer approach.
        # i will just reverse the list from the mid point and then calculate the sums from there.
        # then i will find the maximum sum by iterating through the linkedlists and return it.
        slow = fast = head

        while fast and fast.next: # finding the middle
            fast = fast.next.next 
            slow = slow.next

        slow = reverse(slow) # reversing the second half
        fast = head
        max_sum = 0
        while slow: # iterating through slow and fast  to find the max sum
            if slow.val + fast.val > max_sum:
                max_sum = slow.val + fast.val
            fast = fast.next
            slow= slow.next
        
        return max_sum # return!
