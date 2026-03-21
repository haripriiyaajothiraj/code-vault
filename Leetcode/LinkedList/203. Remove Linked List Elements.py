# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        current = dummy 


        if not head:
            return head
        
        current.next = head 

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next # skip the val or delete the value from linked list
            else:
                current = current.next #move the pointer forward

        return dummy.next