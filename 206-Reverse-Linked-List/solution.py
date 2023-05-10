# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 206-Reverse-Linked-List
""" Logic: Use a loop to go through the linked
           lists, for every iteration we point
           the current element to the previous 
           one and the next element to the
           current one, that way, in the end the
           linkedlist is reversed.
           First: 1 -> 2 -> 3
           Second: None <- 1 -> 2 -> 3
           Third: None <- 1 <- 2 -> 3
           and so on."""

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

   prev = None
   curr = head

   if  curr == None:
       return None

   while curr:
       nex = curr.next
       curr.next = prev
       prev = curr
       curr = nex


   return prev
