# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
 # 142. Linked List Cycle II
""" Logic: Use a loop to go through the linked
           lists, for every iteration we will have
           the single pointer move at half the speed
           of the double pointer. If there is a cycle.
           there will be a point where the single and
           double pointer will meet. Otherwise, we return
           null."""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
            
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                      
            return slow

        return null
            
