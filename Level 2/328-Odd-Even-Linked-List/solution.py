# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: 
            return head # if the list has less than 3 nodes, we can return as it is
        
        odd_head = head # node we will return
        even_head = head.next # this node will be the start of the list containintg the even elements
        odd = odd_head # node for odd element
        even = even_head # node for even element
        # odd_head = 1, even_ head = 2 odd = 1 even = 2
        while even and even.next: # 1 - > 2 - > 3 
            odd.next = even.next # 1-> 3 <- 2
            odd = odd.next # odd_head = 1, even_ head = 2 odd = 3 even = 2 
            even.next = odd.next # 1- > 3  2-> null
            even = even.next # odd_head = 1, even_ head = 2 odd = 3 even = null, since evn is now null, loop ends.
        
        odd.next = even_head # 1- > 3 ->  2 where ordd_head = 1, so we return odd_head
        
        return odd_head # return!
