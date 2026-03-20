class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        p1=0
        for p2 in range(len(s)-1, 0, -1):
            if p1 == p2:
                break
            s[p1],s[p2] = s[p2],s[p1]
            p1 += 1