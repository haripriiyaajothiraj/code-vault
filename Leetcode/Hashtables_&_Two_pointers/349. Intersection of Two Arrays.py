class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dict1 = {}
        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1

        result = []
        for num in nums2:
            if num in dict1 and dict1 > 0:
                result.append(num)
                dict1[num] = 0
        return result