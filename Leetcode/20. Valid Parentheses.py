class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        # stack based problem 
        # Time complexity: O(n)
        # Space complexity: O(n)

        stack = []
        pair_brackets = {"(":")", "{":"}", "[":"]"}
        closing = set(pair_brackets.values()) # O(1) lookup

        if len(s) % 2 != 0:
            return False
            
        for item in s:
            if item in pair_brackets:
                stack.append(item) # storing the open brace 
            elif item in closing:
                if stack and pair_brackets[stack[-1]] == item:
                    stack.pop()
                else:
                    return False
        return not stack