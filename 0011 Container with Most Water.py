class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/

        You are given an integer array height of length n.
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        Notice that you may not slant the container.

        Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
        In this case, the max area of water (blue section) the container can contain is 49.

        Example 2:
        Input: height = [1,1]
        Output: 1

        Constraints:
        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104

        Success Details:
        Runtime: 809 ms, faster than 88.57% of Python3 online submissions for Container With Most Water.
        Memory Usage: 27.4 MB, less than 45.04% of Python3 online submissions for Container With Most Water.

        https://youtu.be/UuiTKBwPgAo
        """

        area = 0                                # initialize area
        l, r = 0, len(height) - 1               # two pointers `l` and `r`
        hi = lambda i: height[i]                # lambda function that returns: height[i]

        while l < r:

            h = min(hi(l) , hi(r))              # choose the lowest between `hi(l)` and `hi(r)`

            area = max(area, h * (r-l))         # store the max area
            
            if hi(l) < hi(r):                   # if hi(l) < hi(r) then
                l += 1                          # increase `l`
            else:                               # otherwise
                r -= 1                          # decrease `r`

        return area
        
