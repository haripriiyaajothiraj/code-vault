# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        # Find the middle 
        """
        use fast and slow pointers
        """
        slow = head 
        fast = head.next 

        while fast and fast.next:
            slow = slow.next #wherever slow pointer stops finally thats the middle
            fast = fast.next.next

        #slow is now pointing the middle node

        # Reverse the second half 
        current = slow 
        prev = None
        nextn = None
        while current:
            nextn = current.next 
            current.next = prev
            prev = current
            current = nextn
        #prev is pointing to the head of the reversed list

        # Verify first and second halves are same
        while head and prev:
            if head.val == prev.val:  # verify if the values are same 
                head = head.next      # Move to next node
                prev = prev.next      # Move to next node
            else:
                return False
        return True
