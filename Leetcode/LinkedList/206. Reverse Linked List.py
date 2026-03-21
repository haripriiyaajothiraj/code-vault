# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        current = head
        next1 = None

        while current:
            next1 = current.next  # save next 
            current.next = prev   # reversing the list 
            prev = current        # move forward 
            current = next1       # move forward
        
        return prev   #new head