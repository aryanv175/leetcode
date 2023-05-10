# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
