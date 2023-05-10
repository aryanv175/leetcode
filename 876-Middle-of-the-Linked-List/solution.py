# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
# 876. Middle of the Linked List
""" Logic: Use a loop to go through the linked
           lists, for every iteration we will have
           the single pointer move at half the speed
           of the double pointer. By the time the double
           pointer reaches the last node or None, the
           single pointer will be at the middle."""
        

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    single, double = head, head

    while double and double.next:
        single = single.next
        double = double.next.next

    return single
