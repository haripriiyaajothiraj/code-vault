class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # return []

        seen = {}
        
        for i,num in enumerate(nums):
                

        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen and i != seen[complement]:
                return[i, seen[complement]]

            seen[num] = i