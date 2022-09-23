class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """

        https://leetcode.com/problems/3sum-closest/

        Given an integer array nums of length n and an integer target,
        find three integers in nums such that the sum is closest to target.

        Return the sum of the three integers.
        You may assume that each input would have exactly one solution.

        Example 1:
        Input: nums = [-1,2,1,-4], target = 1
        Output: 2

        Explanation:
        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

        Example 2:
        Input: nums = [0,0,0], target = 1
        Output: 0


        Constraints:
        3 <= nums.length <= 1000
        -1000 <= nums[i] <= 1000
        -104 <= target <= 104

        """

        nums.sort()											    # sort the nums
        
        closest = float('inf')                                  # `closest` begins from infinity away

        alpha = 0                                               # the beginning
        omega = len(nums) - 1									# the end
        
        while alpha < omega:
            
            _closest = float('inf')                             # current `_closest`

            l = alpha + 1										# `l` left pointer
            r = omega - 1										# `r` right pointer
            
            while l <= r:                                       # while `l` < `r`
                
                m = (l+r) // 2                                  # find middle `m`
                triumph = nums[alpha] + nums[omega] + nums[m]   # get the `triplet_sum`

                if triumph < target:                            # if `triumph` < `target`
                    l = m+1                                     # move `l` forward from `m`

                elif triumph > target:						    # if `triumph` > `target`
                    r = m-1                                     # move `r` backward from `m`

                else:                                           # otherwise `triumph` == `target`
                    return target                               # we got the target
                    
                if abs(triumph-target) < abs(_closest-target):  # if `triumph` is closer than current closest
                    _closest = triumph                          # update current `_closest` to `triumph`
                    
            if _closest < target:                               # if current_closest`<`target`
                alpha += 1                                      # increase `alpha`

            else:											    # otherwise
                omega -= 1                                      # decrease `omega`
                
            if abs(_closest-target) < abs(closest-target):      # if _closest is closer than closest
                closest = _closest                              # update `closest` to current `_closest`
                
        return closest
            
            
            
