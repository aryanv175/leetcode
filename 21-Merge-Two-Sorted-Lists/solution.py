class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 21-Merge-Two-Sorted-Lists
""" Logic: Use a loop to go through the linked
           lists, store the smaller value in the 
           new result linkedlist."""

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  result = ListNode()
  head = result

  while list1 and list2:
      if list1.val < list2.val:
          head.next = list1
          list1 = list1.next
      else:
          head.next = list2
          list2 = list2.next
      head = head.next

  if list1:
      head.next = list1
  elif list2:
      head.next = list2

  return result.next
