# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        """
        Two Pointer Approach:
        pA travels lenA + lenB
        pB travels lenB + lenA
        Both travel same distance!
        Meet at intersection! ✅
        Time: O(n+m), Space: O(1)
        """

        pA = headA
        pB = headB

        while pA != pB:
             # reach end → switch to other list!
            if pA is None:
                pA = headB  # pA switches to listB
            else:
                pA = pA.next  # move forward

            if pB is None:
                pB = headA  # pB switches to listA
            else:
                pB = pB.next  # move forward

        # return the intersection node
        return pA

"""
LC 160 - Intersection of Two Linked Lists

Amazon    ████████████  🔥 Very Frequently Asked!
Microsoft ██████████    🔥 Frequently Asked!
Apple     ████████      ✅ Asked!
Google    ██████        ✅ Asked!
Meta      █████         ✅ Asked!
Adobe     ████████████  🔥 Very Frequently Asked!
Bloomberg ██████████    🔥 Frequently Asked!

🔥 Most Asked By
Plain Text
🥇 Amazon    → Asked in Phone Screen & Onsite!
🥈 Microsoft → Asked in Technical Rounds!
🥉 Adobe     → Very Commonly Asked!

Why FAANG Loves This Problem?
Plain Text
Tests Multiple Concepts:

1️⃣ Linked List Traversal
   → Do you know basics? 🤔

2️⃣ Two Pointer Technique
   → Do you know patterns? 🤔

3️⃣ Memory/Address concept
   → Do you know pointers? 🤔

4️⃣ Edge Cases
   → Do you think carefully? 🤔

5️⃣ Space Optimization
   → Can you do O(1) space? 🤔

What Interviewers Look For
Plain Text
Level 1: Basic Solution ✅
─────────────────────────
HashSet approach
Shows you can solve it
O(n) space

Level 2: Optimal Solution ⭐
──────────────────────────────
Two Pointer approach
Shows pattern knowledge
O(1) space

Level 3: Impress Interviewer 🏆
────────────────────────────────
Explain WHY two pointers work!
"Both travel lenA + lenB distance!"
Handle all edge cases!
Clean code!



🎤 How to Answer in Interview
Step 1️⃣ - Clarify

Ask interviewer:
✅ "Can lists have cycles?"
✅ "Should I preserve list structure?"
✅ "What if no intersection exists?"
✅ "Are values unique?"

Step 2️⃣ - Brute Force First
Plain Text
"Naive approach would be HashSet
 Store all nodes of listA
 Check each node of listB
 Time: O(n+m), Space: O(n)"

Step 3️⃣ - Optimize
Plain Text
"But we can do better!
 Using Two Pointers
 Time: O(n+m), Space: O(1)!"

Step 4️⃣ - Explain Intuition
Plain Text
"Key insight is both pointers
 travel same total distance
 lenA + lenB!
 So they MUST meet at
 intersection!" 🎯

Step 5️⃣ - Code Cleanly
Plain Text
✅ Meaningful variable names
✅ Handle edge cases first
✅ Comment your code
✅ Test with examples


📚 Related Problems FAANG Asks

Linked List Problems Frequently Asked:

Easy:
✅ LC 141 - Linked List Cycle
✅ LC 160 - Intersection (This one!)
✅ LC 83  - Remove Duplicates
✅ LC 21  - Merge Two Sorted Lists

Medium:
✅ LC 142 - Linked List Cycle II
✅ LC 19  - Remove Nth Node from End
✅ LC 2   - Add Two Numbers
✅ LC 143 - Reorder List

Hard:
✅ LC 25  - Reverse Nodes in k-Group
✅ LC 23  - Merge k Sorted Lists
"""