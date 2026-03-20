class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        #Edge case
        if len(s) != len(t):
            return False 
 
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for char in t:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1

        return dict1 == dict2