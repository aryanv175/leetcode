# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # edge case of a empty/ single element linked list
        if not head or not head.next:
            return head
        
        # find the middle of the list as we are going to merge sort.
        # in merge sort we will first sort the parts of the list
        # and then join the merged lists together.

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is currently pointing to the middle element
        # so we can make second_half as the head of the second half of the list 
        # we will also make slow.next = None to disconnect the two halfs of the list

        second_half = slow.next
        slow.next = None

        # now we recursively iterate through the list until we get to smaller halfves of the list

        sorted_first = self.sortList(head)
        sorted_second = self.sortList(second_half)

        # now we merge the two lists
        merged = self.merge(sorted_first, sorted_second)

        return merged # return!
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # this is the function we use to merge the two lists
        # this will be the first element of the list that we want to return, 
        # keep in mind we dont want to return dummy element.
        dummy = ListNode(0) 
        curr = dummy
        
        #iterating through both the lists
        while list1 and list2: # we do this loop until one of the lists finishes
            if list1.val < list2.val: # we add the smaller of the two values as curr.next
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2 # we add the remaining elements to the list

        return dummy.next # return dummy.next as we decided before we dont want to returnt the dummy element!

