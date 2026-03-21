class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if len(ransomNote) > len(magazine):
            return False

        hashmap = {}
        for char in magazine:
            hashmap[char] = hashmap.get(char, 0) + 1

        for char in ransomNote:
            if char in hashmap and hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False
            return True