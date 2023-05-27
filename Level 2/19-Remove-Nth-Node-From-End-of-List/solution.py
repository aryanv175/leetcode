# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target = end = start = ListNode(0, next=head) # make new nodes all that point to the head.
        for i in range(n): # the difference in positions between the end node and the node we want to remove is now n, after we added the new node at the start.
            end = end.next # in the first line
        
        while end.next: # now  we go to the element before the one we want to remove
            target = target.next 
            end = end.next
        
        target.next = target.next.next # removal of the element.
        return start.next # return!
        # we return start.next as start is still pointing to the head of the list.
