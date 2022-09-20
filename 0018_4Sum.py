class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        quadruplets = []
        nums.sort()
		
        for i in range(len(nums) - 3):												# last index on len(nums)-3
			
            if i > 0 and nums[i] == nums[i-1]:										# skip if current number equals previous number
                continue
				
            for j in range(i+1, len(nums)-2):										# next number loop begins with i+1 to len(nums)-2
				
                l, r = j + 1, len(nums) - 1											# two pointers l and r, begins with j+1 to len(nums)-1
				
                while l < r:														# while l < r then keep looping
					
					quadruplet = [ nums[i], nums[j], nums[l], nums[r] ]				# quadruplet
					
                    Sum = sum(quadruplet)											# Sum of quadruplet
					
                    if Sum < target:												# if Sum less than target then increase the `l` index
                        l += 1
						
                    elif Sum > target:												# if Sum greater than target then decrease the `r` index
                        r -= 1
						
                    else:
                        quadruplets.append( quadruplet )			
                        l += 1
						
                        while nums[l] == nums[l-1] and l < r :						# keep skipping if current number equals previous number
                            l += 1													# increase `l` index
							
        Quadruplets = []															# Unique Quadruplets
		
        for quadruplet in list(set(quadruplets)):					
            Quadruplets.append(list(quadruplet))
			
		Quadruplets = list(set(quadruplets)
			
        return Quadruplets
