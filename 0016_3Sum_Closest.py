class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
		Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

		Return the sum of the three integers.

		You may assume that each input would have exactly one solution.

		Example 1:
		
		Input: nums = [-1,2,1,-4], target = 1
		Output: 2
		
		Explanation:
		The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
		"""
		
        nums.sort()											# sort the nums
        
        near = float('inf')                            		# `closest` begins with `far`

        L = 0												# the beginning
        R = len(nums) - 1									# the end										
        
        while L < R:
            
            far = float('inf')                            	# `far` away 

            l = L + 1										# `l` left pointer				
            r = R - 1										# `r` right pointer
            
            while l <= r:									# while `l` < `r`
                
                m = (l+r) // 2                              # find middle `m`
                triple = nums[L] + nums[R] + nums[m]        # get the `triple` sum
                diff = triple - target                      # calculate difference between `triple` and `target`
                
                if diff == 0: return target                 # if `diff` = `0` just return `target`

                if diff > 0:                                # if `diff` > 0
                    r = m-1                                 # decrease the sum by moving `r` towards the left
                else:										# if `diff` < 0
                    l = m+1                                 # increase the sum by moving `l` towards the right
                    
                if abs(diff) < abs(far-target):             # if `diff` is less than the distance `far` to `target` 
                    far = triple                            # update `far` to `triple`
                    
            if (far-target) > 0 :                           # if difference of `far` to `target` is positive 
                R -= 1                                      # decrease the sum by decreasing `R`
            else:											# if difference of `far` to `target` is negative 
                L += 1                                      # increase the sum by increasing `L`
                
            if abs(far-target) < abs(near-target):          # check distance from `near` and `far` to `target` 
                    near = far                              # update `near` to far
                
        return near
            
            
            
