class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        https://youtu.be/q6IEA26hvXc

        Given two sorted arrays nums1 and nums2 of size m and n respectively,
        return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).

        Example 1:
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.

        Example 2:
        Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


        Constraints:
        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -106 <= nums1[i], nums2[i] <= 106

        Discussion:
        https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation
        """
        
        m, n = len(nums1), len(nums2)                                       # store the lengths into variable
        if m < n:                                                           # make sure n is the shortest length 
            return self.findMedianSortedArrays(nums2, nums1)
                                                                              
        L, R = 0, n * 2                                                     # shortest imaginary placeholder named LOVER where they need to find V  
                                                                            # with max length equals twice the length of the shortest array
                                                                            # we are going to find the max(L1, L2) and min(R1, R2)
                                                                            # the LOVER will meet at the median value V
                                                                            # where V is the average of ( max(L1,L2) + min(R1,R2) )
                                                                            # we will keep on searching as long as L <= R
                                                                            # we will stop when L > R as we got the max(L1, L2) or equivalently min(R1,R2)
        
        while L <= R:
        
            v2 = (L + R) // 2                                               # v2 is the midpoint of L and R
            v1 = m + n - v2                                               
            
            
            L1 = float('-inf') if v1 == 0 else nums1[ (v1 - 1) // 2]        # corner case at v1 == 0, imagine float('-inf') value
            L2 = float('-inf') if v2 == 0 else nums2[ (v2 - 1) // 2]        # corner case at v2 == 0, imagine float('-inf') value
            
            R1 = float('inf') if v1 == 2 *m else nums1[ v1 // 2]           # corner case at v1 == 2 *m, imagine float('inf') value
            R2 = float('inf') if v2 == 2 *n else nums2[ v2 // 2]           # corner case at v2 == 2 *n, imagine float('inf') value
            
            L1 < R1 == True                                                 # every L1 < R1 because the array is sorted
            L2 < R2 == True                                                 # every L2 < R2 because the array is sorted

            if L1 > R2:                                                     # when there are more smaller numbers on L1 than on R2
                L = v2 + 1                                                  # we need to shift v1 toward the smaller, hence shift v2 toward the greater
                                                                            
            elif L2 > R1:                                                   # when there are more smaller numbers on L2 than on R1
                R = v2 - 1                                                  # we need to shift v2 toward the smaller            
                
            else:
                return ( max(L1, L2) + min(R1, R2) ) / 2.0                  

