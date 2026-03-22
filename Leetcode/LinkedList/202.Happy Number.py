class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        using floyd algorithm because unhappy numbers meet at repeation
        use fast and slow pointers to find meeting point 
        Time complexity : O(log n)
        Space complexity : O(1)
        """
        
        
        # find the cyle and break the loop 
        # handle this as a linked list 
        # Nodes are connected as sum_of_squares(n) ---> next number
        # Same number will be visited twice
        # floyd algo on numbers to find cycle detection 

        #sum_of_squares = 1 #Happy number
        #sum_of_squares = breaks at meeting of the cycle  #Number is not happy

        def sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                num = num // 10
                total += digit * digit
            return total

        slow = n 
        fast = n

        while True:
            slow = sum_of_squares(slow) #Move 1 step
            if slow == 1:
                return True # Happy number 
            fast = sum_of_squares(sum_of_squares(fast))  #Move 2 steps
            if fast == 1:
                return True # Happy number         
            if slow == fast:
                return False  # pointers are met hence cycle is occured and the number is not happy


        
            
