class Solution:
    def trap(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/trapping-rain-water/

        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.

        Example 1:

        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water (blue section) are being trapped.

        Example 2:

        Input: height = [4,2,0,3,2,5]
        Output: 9


        Constraints:

        n == height.length
        1 <= n <= 2 * 104
        0 <= height[i] <= 105

        """

        water = 0                               # initialize water
        l, r = 0, len(height) - 1               # two pointers `l` and `r`
        hi = lambda i: height[i]                # lambda function that returns: height[i]
        hl, hr = hi(l), hi(r)                   # initialize `hl` and `hr`

        while l < r:

            if hi(l) < hi(r):                   # compare `hi(l)` and `hi(r)`
                l += 1                          # increase `l` by 1
                hl = max(hl, hi(l))             # choose the max and keep the max
                water += hl - hi(l)             # difference between peak and current height

            else:
                r -= 1                          # decrease `r` by 1
                hr = max(hr, hi(r))             # choose the max and keep the max
                water += hr - hi(r)             # difference between peak and current height

        return water