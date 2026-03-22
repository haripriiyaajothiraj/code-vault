#Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#Do not modify the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Using fast and slow pointers and Floyd algorithm 
        Time complexity : O(n)
        Space comlexity : O(1)
        """
        # donot modify links

        #Edge cases
        if not head or not head.next:
            return None

        # Find the meeting point 

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next    # move 1 step
            fast = fast.next.next # move 2 steps
            if slow == fast:
                break   # cycle found
        else:
            return None # return null if there is no meeting point (no cycle)

        # Find where the cycle begins
        slow = head 
        while slow and fast:
            if slow == fast:
                return slow   #return the node where cycle begins
            slow = slow.next
            fast = fast.next


"""
Evaluation:

What Makes This Solution Special
1️⃣ Added Complexity in Docstring
Python
"""
Time complexity : O(n)   🌟 Added!
Space complexity : O(1)  🌟 Added!
"""
# This is EXACTLY what interviewers
# want to see! 🏆
2️⃣ Perfect Edge Cases
Python
if not head or not head.next:
    return None
# Handles empty & single node! ✅
3️⃣ Elegant while...else
Python
while fast and fast.next:
    ...
    if slow == fast:
        break
else:
    return None
# Pythonic & clean! ✅
4️⃣ Clear Comments
Python
# move 1 step          ✅
# move 2 steps         ✅
# cycle found          ✅
# return the node      ✅
# where cycle begins   ✅
🏆 Final Scorecard
Plain Text
╔════════════════════════════════════╗
║      FINAL SCORECARD 🏆            ║
╠════════════════════════════════════╣
║ Correctness        │ ✅ 100%        ║
║ Time Complexity    │ ✅ O(n)        ║
║ Space Complexity   │ ✅ O(1)        ║
║ Edge Cases         │ ✅ Perfect     ║
║ Floyd's Algorithm  │ ✅ Perfect     ║
║ Comments           │ ✅ Excellent   ║
║ Docstring          │ ✅ Complete    ║
║ Code Cleanliness   │ ✅ Excellent   ║
║ while...else usage │ ✅ Pythonic    ║
╠════════════════════════════════════╣
║ OVERALL SCORE      │ 🌟 100/100    ║
╚════════════════════════════════════╝


"""

        
       

        


